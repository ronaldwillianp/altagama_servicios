#################################################################################################
#                                       Clientes                                                #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_cliente_administrar():
    if not request.args(0):
        redirect(URL('contrato','contrato_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato','contrato_cliente_administrar'))
    
    firmas_contrato = db(
        db.firma_autorizada_contrato_cliente.contrato==registro.id
        ).select()
    
    rows = []
    for row in firmas_contrato:
        rows.append(db(db.firma_autorizada.id == row.firma_autorizada).select().as_list()[0])
    
    return dict(rows=rows, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_cliente_crear():
    if not request.args(0):
        redirect(URL('contrato','contrato_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato','contrato_cliente_administrar'))

    form = SQLFORM(db.firma_autorizada)

    if form.process().accepted:
        id_firma = form.vars.id
        db.firma_autorizada_contrato_cliente.validate_and_insert(
            firma_autorizada = id_firma,
            contrato = registro.id
        )
        session.status = True
        session.msg = 'Firma creada correctamente'
        redirect(URL('firma_autorizada', 'firma_autorizada_cliente_administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)


@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_cliente_eliminar():
    if not request.args(0):
        redirect(URL('contrato','contacto_cliente_administrar'))
    if not request.args(1):
        redirect(URL('contrato','contacto_cliente_administrar'))
    id_contrato = request.args(0)
    id_firma = request.args(1)
    registro = db.firma_autorizada(request.args(1, cast=int)) or redirect(URL('contrato','contacto_cliente_administrar'))
    db(db.firma_autorizada.id == registro.id).delete()
    session.status = True
    session.msg = 'Firma eliminada correctamente'
    redirect(URL('firma_autorizada', 'firma_autorizada_cliente_administrar', args = id_contrato))
    return dict()

#################################################################################################
#                                       Proveedores                                             #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_proveedor_administrar():
    if not request.args(0):
        redirect(URL('contrato','contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato','contrato_proveedor_administrar'))
    
    firmas_contrato = db(
        db.firma_autorizada_contrato_proveedor.contrato==registro.id
        ).select()
    
    rows = []
    for row in firmas_contrato:
        rows.append(db(db.firma_autorizada.id == row.firma_autorizada).select().as_list()[0])
    
    return dict(rows=rows, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_proveedor_crear():
    if not request.args(0):
        redirect(URL('contrato','contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato','contrato_proveedor_administrar'))

    form = SQLFORM(db.firma_autorizada)

    if form.process().accepted:
        id_firma = form.vars.id
        db.firma_autorizada_contrato_proveedor.validate_and_insert(
            firma_autorizada = id_firma,
            contrato = registro.id
        )
        session.status = True
        session.msg = 'Firma creada correctamente'
        redirect(URL('firma_autorizada', 'firma_autorizada_proveedor_administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)


@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def firma_autorizada_proveedor_eliminar():
    if not request.args(0):
        redirect(URL('contrato','contacto_proveedor_administrar'))
    if not request.args(1):
        redirect(URL('contrato','contacto_proveedor_administrar'))
    id_contrato = request.args(0)
    id_firma = request.args(1)
    registro = db.firma_autorizada(request.args(1, cast=int)) or redirect(URL('contrato','contacto_proveedor_administrar'))
    db(db.firma_autorizada.id == registro.id).delete()
    session.status = True
    session.msg = 'Firma eliminada correctamente'
    redirect(URL('firma_autorizada', 'firma_autorizada_proveedor_administrar', args = id_contrato))
    return dict()
