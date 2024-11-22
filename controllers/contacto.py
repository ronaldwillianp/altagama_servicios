@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def administrar():
    if not request.args(0):
        redirect(URL('contrato','administrar'))

    registro = db.contrato(request.args(0, cast=int)
                           ) or redirect(URL('contrato','administrar'))
    rows = db(db.contacto.contrato == registro.id).select()
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def preprocess_contacto(form):
    nombre = form.vars.nombre
    numero = form.vars.numero
    contrato = form.vars.contrato
    
    contacto_db = db(
        (db.contacto.nombre == nombre) &
        (db.contacto.numero == numero) &
        (db.contacto.contrato == contrato)
    ).count()


    if contacto_db>0:
        form.errors.numero = 'Ya existe este contacto en la empresa actual'

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def crear():
    if not request.args(0):
        redirect(URL('contrato','administrar'))

    registro = db.contrato(request.args(0, cast=int)) or redirect(URL('contrato','administrar'))

    db.contacto.contrato.writable = False
    form = SQLFORM(db.contacto)
    form.vars.contrato = registro.id

    if form.process(onvalidation=preprocess_contacto).accepted:
        session.status = True
        session.msg = 'Contacto creado correctamente'
        redirect(URL('contacto', 'administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def eliminar():
    if not request.args(0):
        redirect(URL('contrato','administrar'))

    registro = db.contacto(request.args(0, cast=int)
                           ) or redirect(URL('contrato','administrar'))
    x = registro.id

    contrato = None
    if session.contrato:
        contrato = session.contrato
        del(session.contrato)

    db(db.contacto.id == x).delete()
    session.status = True
    session.msg = 'Contacto eliminado correctamente'

    if contrato != None:
        redirect(URL("contacto","administrar", args=contrato))
    else:
        redirect(URL("contrato","administrar"))

    return dict()

