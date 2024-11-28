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
    
    contactos = db(db.contacto.contrato == registro.id).select()
    firmas = db(db.firma_autorizada.contrato == registro.id).select()
    return dict(contrato=registro, contactos=contactos, firmas=firmas)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def contrato_cliente_administrar():
    rows = db(
        (db.contrato_cliente.id > 0)  &
        (db.contrato_cliente.anho == get_current_year)
        ).select(
            orderby=db.contrato_cliente.id
        )
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def preprocess_contrato(form):
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
def postprocess_contrato(form):
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
    if form.process(onvalidation=preprocess_contrato).accepted:
        session.status = True
        session.msg = 'Contrato creado correctamente'
        # redirect(URL('contacto','crear', args=form.vars.id))
        redirect(URL('contrato','contrato_cliente_administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

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

    if form.process(onvalidation=postprocess_contrato).accepted:
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
def contrato_cliente_elimina():
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