@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def reporte_contrato_cliente():
    contratos = []
    ids = []

    clientes = db(db.contrato_cliente.id>0).select(
        db.contrato_cliente.id, 
        db.contrato_cliente.empresa, 
        orderby=db.contrato_cliente.empresa, 
        groupby=db.contrato_cliente.empresa
        ).as_list()

    # Si viene alguna peticion especifica de la vista para filtrar determinados clientes
    if request.vars:
        # Las peticiones pueden ser vacias, de un elemento(str) o multiples(list)
        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <list>
        if isinstance(request.vars['cliente'], list) :
            ids = list(map(int, request.vars['cliente']))
            
            for i in ids:
                row = db(db.contrato_cliente.id == i).select()
                contratos.append(row[0])

            # Agrega el campo 'selected' (True/False), a los registros de cliente para poder saber cuales estan seleccionados y cuales no
            for cliente in clientes:
                if cliente['id'] in ids:
                    cliente['selected'] = True
                else:
                    cliente['selected'] = False

        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <str>
        elif type(request.vars['cliente']) == str:
            # Com es instancia de <str> quiere decir que es un solo id, por lo que selecciona este unico cliente
            id = int(request.vars['cliente'])
            contratos.append(db.contrato_cliente[id])

            for i in clientes:
                if i['id'] == id:
                    i['selected'] = True
                else:
                    i['selected'] = False

    # En caso de que la peticion se pase vacia, se devolvera siempre todos los mantenimientos para evitar incongruencias
    else:
        for i in clientes:
            i['selected'] = False

    return dict(clientes=clientes, contratos=contratos)

@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Jurídico')
)
def reporte_contrato_proveedor():
    contratos = []
    ids = []

    proveedores = db(db.contrato_proveedor.id>0).select(
        db.contrato_proveedor.id, 
        db.contrato_proveedor.empresa, 
        orderby=db.contrato_proveedor.empresa, 
        groupby=db.contrato_proveedor.empresa
        ).as_list()

    # Si viene alguna peticion especifica de la vista para filtrar determinados clientes
    if request.vars:
        # Las peticiones pueden ser vacias, de un elemento(str) o multiples(list)
        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <list>
        if isinstance(request.vars['proveedor'], list) :
            ids = list(map(int, request.vars['proveedor']))
            
            for i in ids:
                row = db(db.contrato_proveedor.id == i).select()
                contratos.append(row[0])

            # Agrega el campo 'selected' (True/False), a los registros de cliente para poder saber cuales estan seleccionados y cuales no
            for proveedor in proveedores:
                if proveedor['id'] in ids:
                    proveedor['selected'] = True
                else:
                    proveedor['selected'] = False

        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <str>
        elif type(request.vars['proveedor']) == str:
            # Com es instancia de <str> quiere decir que es un solo id, por lo que selecciona este unico cliente
            id = int(request.vars['proveedor'])
            contratos.append(db.contrato_proveedor[id])

            for i in proveedores:
                if i['id'] == id:
                    i['selected'] = True
                else:
                    i['selected'] = False

    # En caso de que la peticion se pase vacia, se devolvera siempre todos los mantenimientos para evitar incongruencias
    else:
        for i in proveedores:
            i['selected'] = False

    return dict(proveedores=proveedores, contratos=contratos)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def reporte_mantenimiento():
    # Listado de clientes de la BD que reciben servicios [Para poder asignar mantenimiento]
    clientes = db(
        (db.contrato_cliente.id > 0) &
        (db.contrato_cliente.tipo_contrato == 'sv')
    ).select()

    # Si viene alguna peticion especifica de la vista para filtrar determinados clientes
    if request.vars:
        # Las peticiones pueden ser vacias, de un elemento(str) o multiples(list)
        contratos = []
        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <list>
        if isinstance(request.vars['proveedor'], list) :
            ids = list(map(int, request.vars['proveedor']))
            # Se recorren las entidades seleccionadas y se seleccionan sus mantenimientos
            for i in ids:
                for mantenimiento in db(db.mantenimiento.contrato == i).select():
                    contratos.append(mantenimiento)

            # Agrega el campo 'selected' (True/False), a los registros de cliente para poder saber cuales estan seleccionados y cuales no
            for cliente in clientes:
                if cliente.id in ids:
                    cliente['selected'] = True
                else:
                    cliente['selected'] = False

        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <str>
        elif type(request.vars['proveedor']) == str:
            print(1)
            # Com es instancia de <str> quiere decir que es un solo id, por lo que selecciona solo los mantenimientos de este unico cliente
            for mantenimiento in db(db.mantenimiento.contrato == request.vars['proveedor']).select():
                contratos.append(mantenimiento)
            print('Hereee')

            for cliente in clientes:
                # Esta parte se encarga de agregarle a los rows un valor 'selected' de tipo <boolean> para contrlar si un registro ha sid seleccinado o no para la vista del dropdown
                # En este caso es necesario convertir el valor que viene de la vista de tipo <str> a <int> o el query no lo toma en cuenta
                if cliente.id == int(request.vars['proveedor']):
                    cliente['selected'] = True
                else:
                    cliente['selected'] = False
    # En caso de que la peticion se pase vacia, se devolvera siempre todos los mantenimientos para evitar incongruencias
    else:
        contratos = []
        # Esta parte se encarga de agregarle a los rows un valor 'selected' de tipo <boolean> para contrlar si un registro ha sid seleccinado o no para la vista del dropdown
        for cliente in clientes:
            cliente['selected'] = False

    return dict(contratos=contratos, clientes=clientes)

