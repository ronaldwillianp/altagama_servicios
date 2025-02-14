@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def reporte_contrato():
    cliente = None
    anho = None
    contratos = []

    clientes = db(db.contrato_cliente.id>0).select(db.contrato_cliente.id, db.contrato_cliente.empresa, orderby=db.contrato_cliente.empresa,  groupby=db.contrato_cliente.empresa).as_list()

    if request.vars['anho']:
        anho = request.vars['anho']

    if request.vars['cliente']:
        # print(request.vars['cliente'])
        pass

    else:
        contratos = db(
            (db.contrato_cliente.anho == anho)
        ).select()

    return dict(clientes=clientes)