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
    rows = db(db.firma_autorizada.contrato == registro.id).select()
    return dict(rows=rows)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def crear():
    if not request.args(0):
        redirect(URL('contrato','administrar'))

    registro = db.contrato(request.args(0, cast=int)) or redirect(URL('contrato','administrar'))

    db.firma_autorizada.contrato.writable = False
    form = SQLFORM(db.firma_autorizada)
    form.vars.contrato = registro.id

    if form.process().accepted:
        session.status = True
        session.msg = 'Firma registrada correctamente'
        redirect(URL('firma_autorizada', 'administrar', args=registro.id))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def eliminar():
    if not request.args(0):
        redirect(URL('contrato','administrar'))

    registro = db.firma_autorizada(request.args(0, cast=int)
                           ) or redirect(URL('contrato','administrar'))
    x = registro.id

    contrato = None
    if session.contrato:
        contrato = session.contrato
        del(session.contrato)

    db(db.firma_autorizada.id == x).delete()
    session.status = True
    session.msg = 'Firma eliminada correctamente'

    if contrato != None:
        redirect(URL("firma_autorizada","administrar", args=contrato))
    else:
        redirect(URL("contrato","administrar"))
        
    return dict()

