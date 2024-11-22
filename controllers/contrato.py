@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def detalles():
    return dict()

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def administrar():
    if session.contrato: del(session.contrato)
    rows = db(db.contrato.id > 0).select()
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def preprocess_contrato(form):
    numero = form.vars.numero
    empresa = form.vars.empresa
    naturaleza = form.vars.naturaleza
    tipo_contrato = form.vars.tipo_contrato

    contrato_db = db(
        (db.contrato.numero == numero) &
        (db.contrato.empresa == empresa) &
        (db.contrato.naturaleza == naturaleza) &
        (db.contrato.tipo_contrato == tipo_contrato)
    ).count()

    if contrato_db>0:
        form.errors.numero = 'Ya existe este contrato'

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def crear():
    form = SQLFORM(db.contrato)
    if form.process(onvalidation=preprocess_contrato).accepted:
        session.status = True
        session.msg = 'Contrato creado correctamente'
        redirect(URL('contacto','crear', args=form.vars.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def editar():
    if not request.args(0):
        redirect(URL('index'))

    registro = db.contrato(request.args(0, cast=int)
                            ) or redirect(URL('index'))

    form = SQLFORM(db.contrato, registro)
    if form.process(onvalidation=preprocess_contrato).accepted:
        session.status = True
        session.msg = 'Contrato actualizado correctamente'
        redirect(URL('administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, registro=registro)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def eliminar():
    if not request.args(0):
        redirect(URL('administrar'))

    registro = db.contrato(request.args(0, cast=int)
                           ) or redirect(URL('administrar'))
    x = registro.id

    db(db.contrato.id == x).delete()
    session.status = True
    session.msg = 'Contrato eliminado correctamente'
    redirect(URL("administrar"))

    return dict()
