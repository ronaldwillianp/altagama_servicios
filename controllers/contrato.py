#################################################################################################
#                                       Clientes                                                #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_detalles():
    if not request.args(0):
        redirect(URL('contrato','contrato_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)
                            ) or redirect(URL('contrato','contrato_cliente_administrar'))
    
    contactos = db(
        db.contacto_contrato_cliente.contrato == registro.id

    ).select(
        db.contacto.nombre,
        db.contacto.numero,
        db.contacto.tipo,
        db.contacto.cargo
    )
    firmas = db(
        db.firma_autorizada_contrato_cliente.contrato == registro.id

    ).select(
        db.firma_autorizada.nombre_completo,
        db.firma_autorizada.cargo
    )
    return dict(contrato=registro, contactos=contactos, firmas=firmas)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_administrar():
    rows = db(
        (db.contrato_cliente.id > 0) &
        (db.contrato_cliente.estado_contrato != 'ar')
        ).select(
            orderby=db.contrato_cliente.id
        )
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def preprocess_contrato_cliente(form):
    numero = form.vars.numero
    anho = form.vars.anho
    tipo_contrato = form.vars.tipo_contrato

    contratos = db(
        (db.contrato_cliente.numero == numero) &
        (db.contrato_cliente.anho == anho) &
        (db.contrato_cliente.tipo_contrato == tipo_contrato)
    ).count()

    if contratos > 0:
        form.errors.numero = 'Ya existe un contrato este número.'
        form.errors.anho = 'Ya existe un contrato este año.'
        form.errors.tipo_contrato = 'Ya existe un contrato de este tipo.'

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def postprocess_contrato_cliente(form):
    numero = form.vars.numero
    anho = form.vars.anho
    tipo_contrato = form.vars.tipo_contrato
    cliente_id = form.vars.cliente_id

    contratos = db(
        (db.contrato_cliente.numero == numero) &
        (db.contrato_cliente.anho == anho) &
        (db.contrato_cliente.tipo_contrato == tipo_contrato) &
        (db.contrato_cliente.id != cliente_id)
    ).count()

    if contratos > 0:
        form.errors.numero = 'Ya existe un contrato este número.'
        form.errors.anho = 'Ya existe un contrato este año.'
        form.errors.tipo_contrato = 'Ya existe un contrato de este tipo.'
    

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_crear():
    form = SQLFORM(db.contrato_cliente)
    # Obtain the IDs of users with the 'Servicios' role
    query = (db.auth_membership.group_id == db(db.auth_group.role == 'Servicios').select(db.auth_group.id).first().id)
    rows = db(query).select(db.auth_membership.user_id)

    # Extract user IDs into a list
    user_ids = [row.user_id for row in rows]

    if form.process(onvalidation=preprocess_contrato_cliente).accepted:
        db.notificacion_sistema.validate_and_insert(titulo="Nueva Notificación", mensaje="Contrato agregado al sistema", usuarios=user_ids)
        session.status = True
        session.msg = 'Contrato creado correctamente'
        # redirect(URL('contacto','crear', args=form.vars.id))
        redirect(URL('contrato','contrato_cliente_administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    # return dict(form=form)
    return locals()

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_editar():
    if not request.args(0):
        redirect(URL('contrato_cliente_administrar'))
        

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato_cliente_administrar'))

    form = SQLFORM(db.contrato_cliente, registro)
    form.vars.cliente_id = registro.id

    if form.process(onvalidation=postprocess_contrato_cliente).accepted:
        session.status = True
        session.msg = 'Contrato actualizado correctamente'
        redirect(URL('contrato_cliente_administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_eliminar():
    if not request.args(0):
        redirect(URL('contrato_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato_cliente_administrar'))

    db(db.contrato_cliente.id == registro.id).delete()
    session.status = True
    session.msg = 'Contrato eliminado correctamente'
    redirect(URL("contrato_cliente_administrar"))

    return dict()

@cache.action()
def contrato_cliente_stream_pdf():
    if not request.args(0):
        redirect(URL('contrato_cliente_administrar'))
    pdf = request.args(0)
    (filename, route) = db.contrato_cliente.contrato_file.retrieve(pdf, nameonly=True)
    return response.stream(route)

#################################################################################################
#                                       Proveedores                                             #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_proveedor_detalles():
    if not request.args(0):
        redirect(URL('contrato','contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)
                            ) or redirect(URL('contrato','contrato_proveedor_administrar'))
    
    contactos = db(
        db.contacto_contrato_proveedor.contrato == registro.id

    ).select(
        db.contacto.nombre,
        db.contacto.numero,
        db.contacto.tipo,
        db.contacto.cargo
    )
    firmas = db(
        db.firma_autorizada_contrato_proveedor.contrato == registro.id

    ).select(
        db.firma_autorizada.nombre_completo,
        db.firma_autorizada.cargo
    )
    return dict(contrato=registro, contactos=contactos, firmas=firmas)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico'))
def contrato_proveedor_administrar():
    rows = db(
        (db.contrato_proveedor.id > 0) &
        (db.contrato_proveedor.estado_contrato != 'ar')
        ).select(
            orderby=db.contrato_proveedor.id
        )
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def preprocess_contrato_proveedor(form):
    numero = form.vars.numero
    anho = form.vars.anho
    tipo_contrato = form.vars.tipo_contrato

    contratos = db(
        (db.contrato_proveedor.numero == numero) &
        (db.contrato_proveedor.anho == anho) &
        (db.contrato_proveedor.tipo_contrato == tipo_contrato)
    ).count()

    if contratos > 0:
        form.errors.numero = 'Ya existe un contrato este número.'
        form.errors.anho = 'Ya existe un contrato este año.'
        form.errors.tipo_contrato = 'Ya existe un contrato de este tipo.'

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def postprocess_contrato_proveedor(form):
    numero = form.vars.numero
    anho = form.vars.anho
    tipo_contrato = form.vars.tipo_contrato
    cliente_id = form.vars.cliente_id

    contratos = db(
        (db.contrato_proveedor.numero == numero) &
        (db.contrato_proveedor.anho == anho) &
        (db.contrato_proveedor.tipo_contrato == tipo_contrato) &
        (db.contrato_proveedor.id != cliente_id)
    ).count()

    if contratos > 0:
        form.errors.numero = 'Ya existe un contrato este número.'
        form.errors.anho = 'Ya existe un contrato este año.'
        form.errors.tipo_contrato = 'Ya existe un contrato de este tipo.'
    

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_proveedor_crear():
    form = SQLFORM(db.contrato_proveedor)
    if form.process(onvalidation=preprocess_contrato_proveedor).accepted:
        session.status = True
        session.msg = 'Contrato creado correctamente'
        # redirect(URL('contacto','crear', args=form.vars.id))
        redirect(URL('contrato','contrato_proveedor_administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_proveedor_editar():
    if not request.args(0):
        redirect(URL('contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato_proveedor_administrar'))

    form = SQLFORM(db.contrato_proveedor, registro)
    form.vars.cliente_id = registro.id

    if form.process(onvalidation=postprocess_contrato_proveedor).accepted:
        session.status = True
        session.msg = 'Contrato actualizado correctamente'
        redirect(URL('contrato_proveedor_administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_proveedor_eliminar():
    if not request.args(0):
        redirect(URL('contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato_proveedor_administrar'))

    db(db.contrato_proveedor.id == registro.id).delete()
    session.status = True
    session.msg = 'Contrato eliminado correctamente'
    redirect(URL("contrato_proveedor_administrar"))

    return dict()

@cache.action()
def contrato_cliente_stream_pdf():
    if not request.args(0):
        redirect(URL('contrato_cliente_administrar'))
    pdf = request.args(0)
    (filename, route) = db.contrato_cliente.contrato_file.retrieve(pdf, nameonly=True)
    return response.stream(route)
