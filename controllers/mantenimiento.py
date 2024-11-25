@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo')
)
def detalles():
    return dict()

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def contrato_servicio_mantenimiento():
    rows = db(
        (db.contrato.id > 0) &
        (db.contrato.estado_contrato == 'ar') &
        (db.contrato.tipo_contrato == 'cl') &
        (db.contrato.naturaleza == 'sv')
        ).select(
            db.contrato.id,
            db.contrato.numero,
            db.contrato.empresa,
            db.mantenimiento_contrato.id,
            left=db.mantenimiento_contrato.on(db.contrato.id==db.mantenimiento_contrato.contrato)
        )
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def habilitar_mantenimiento():
    registro = db.contrato(request.args(0, cast=int)) or redirect(URL('contrato_servicio_mantenimiento'))
    
    db.mantenimiento_contrato.contrato.writable = False
    form = SQLFORM(db.mantenimiento_contrato)
    form.vars.contrato = registro.id
    
    if form.process().accepted:
        session.status = True
        session.msg = 'Mantenimiento habilitado para este contrato'
        redirect(URL('mantenimiento','contrato_servicio_mantenimiento'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def deshabilitar_mantenimiento():
    registro = db.contrato(request.args(0, cast=int)) or redirect(URL('administrar'))
    row = db(db.mantenimiento_contrato.contrato == registro.id).select().first()    
    mantenimientos = db(db.mantenimiento.mantenimiento_contrato == row.id).count()

    if mantenimientos>0:
        session.error = True
        session.msg = 'No es posible deshabilitar. Este contrato tiene mantenimientos.'    
    else:
        db(db.mantenimiento_contrato.id == row.id).delete()
        session.status = True
        session.msg = 'Mantenimiento deshabilitado para este contrato'
    redirect(URL('mantenimiento','contrato_servicio_mantenimiento'))    
    return dict()

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def administrar():
    registro = db.mantenimiento_contrato(request.args(0, cast=int)) or redirect(URL('contrato_servicio_mantenimiento'))
    rows = db(
        (db.contrato.id == registro.contrato) &
        (db.mantenimiento.mantenimiento_contrato == registro.id)
    ).select(
        db.mantenimiento.id,
        db.mantenimiento.fecha,
        db.mantenimiento.cantidad_pc,
        orderby=db.mantenimiento.fecha|~db.mantenimiento.id
    )
    contrato = db(db.contrato.id == registro.contrato).select(
        db.contrato.id,
        db.contrato.numero,
        db.contrato.empresa,
    ).first()

    return dict(rows=rows, contrato=contrato)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def crear():
    registro = db.mantenimiento_contrato(request.args(0, cast=int)) or redirect(URL('mantenimiento','contrato_servicio_mantenimiento'))
    
    db.mantenimiento.mantenimiento_contrato.writable = False
    form = SQLFORM(db.mantenimiento)
    form.vars.mantenimiento_contrato = registro.id
    
    if form.process().accepted:
        session.status = True
        session.msg = 'Mantenimiento agregado correctamente'
        redirect(URL('mantenimiento','administrar', args = registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def editar():

    if not request.args(1):
        redirect(URL('mantenimiento','contrato_servicio_mantenimiento'))

    if not request.args(0):
        redirect(URL('mantenimiento','administrar', args=request.args(0)))

    registro = db.mantenimiento(request.args(0, cast=int)) or redirect(URL('mantenimiento','administrar', args=request.args(1)))
    
    db.mantenimiento.mantenimiento_contrato.writable = False
    
    form = SQLFORM(db.mantenimiento, registro)
    if form.process().accepted:
        session.status = True
        session.msg = 'Mantenimiento actualizado correctamente'
        redirect(URL('mantenimiento', 'administrar', args=request.args(1)))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def eliminar():
    if not request.args(0):
        redirect(URL('mantenimiento','contrato_servicio_mantenimiento'))

    mantenimiento_contrato = None
    if session.mantenimiento_contrato:
        mantenimiento_contrato = session.mantenimiento_contrato
        del(session.mantenimiento_contrato)

    registro = db.mantenimiento(request.args(0, cast=int)
                           ) or redirect(URL('mantenimiento','administrar', args=mantenimiento_contrato))
    x = registro.id

    db(db.mantenimiento.id == x).delete()
    session.status = True
    session.msg = 'Mantenimiento eliminado correctamente'
    redirect(URL("mantenimiento","administrar", args=mantenimiento_contrato))

    return dict()


