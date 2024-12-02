#################################################################################################
#                                       Clientes                                                #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_cliente_administrar():
    if not request.args(0):
        redirect(URL('contrato','contrato_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato','contrato_cliente_administrar'))
    
    contactos_contrato = db(
        db.contacto_contrato_cliente.contrato==registro.id
        ).select()
    
    rows = []
    for row in contactos_contrato:
        rows.append(db(db.contacto.id == row.contacto).select().as_list()[0])
    
    return dict(rows=rows, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_cliente_crear():
    if not request.args(0):
        redirect(URL('contrato','contacto_cliente_administrar'))

    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato','contacto_cliente_administrar'))

    form = SQLFORM(db.contacto)

    if form.process().accepted:
        id_contacto = form.vars.id
        db.contacto_contrato_cliente.validate_and_insert(
            contacto = id_contacto,
            contrato = registro.id
        )
        session.status = True
        session.msg = 'Contacto creado correctamente'
        redirect(URL('contacto', 'contacto_cliente_administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)


@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_cliente_eliminar():
    if not request.args(0):
        redirect(URL('contrato','contacto_cliente_administrar'))
    if not request.args(1):
        redirect(URL('contrato','contacto_cliente_administrar'))
    registro = db.contacto(request.args(1, cast=int)) or redirect(URL('contrato','contacto_cliente_administrar'))
    db(db.contacto.id == registro.id).delete()
    session.status = True
    session.msg = 'Contacto eliminado correctamente'
    redirect(URL('contacto', 'contacto_cliente_administrar', args = request.args(0)))
    return dict()

#################################################################################################
#                                       Proveedores                                             #
#################################################################################################
@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_proveedor_administrar():
    if not request.args(0):
        redirect(URL('contrato','contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato','contrato_proveedor_administrar'))
    
    contactos_contrato = db(
        db.contacto_contrato_proveedor.contrato==registro.id
        ).select()
    
    rows = []
    for row in contactos_contrato:
        rows.append(db(db.contacto.id == row.contacto).select().as_list()[0])
    
    return dict(rows=rows, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_proveedor_crear():
    if not request.args(0):
        redirect(URL('contrato','contrato_proveedor_administrar'))

    registro = db.contrato_proveedor(request.args(0, cast=int)) or redirect(URL('contrato','contrato_proveedor_administrar'))

    form = SQLFORM(db.contacto)

    if form.process().accepted:
        id_contacto = form.vars.id
        db.contacto_contrato_proveedor.validate_and_insert(
            contacto = id_contacto,
            contrato = registro.id
        )
        session.status = True
        session.msg = 'Contacto creado correctamente'
        redirect(URL('contacto', 'contacto_proveedor_administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)


@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contacto_proveedor_eliminar():
    if not request.args(0):
        redirect(URL('contrato','contacto_proveedor_administrar'))
    if not request.args(1):
        redirect(URL('contrato','contacto_proveedor_administrar'))
    registro = db.contacto(request.args(1, cast=int)) or redirect(URL('contrato','contrato_proveedor_administrar'))
    db(db.contacto.id == registro.id).delete()
    session.status = True
    session.msg = 'Contacto eliminado correctamente'
    redirect(URL('contacto', 'contacto_proveedor_administrar', args = request.args(0)))
    return dict()