@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def get_mantenimiento_semanal():
    mantenimientos = db(
        (db.mantenimiento.fecha >= datetime.datetime.now()) &
        (db.mantenimiento.fecha < (datetime.datetime.now() + datetime.timedelta(days=7))) &
        (db.mantenimiento.estado != 'ca') &
        (db.mantenimiento.estado != 'ej')
        ).select()
    return dict(mantenimientos=mantenimientos)

@auth.requires(
    auth.has_membership(role='Administrador') or 
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def get_mantenimiento_mismo_dia():
    mantenimientos = db(
        (db.mantenimiento.fecha >= datetime.datetime.now())
        ).select(
        )
    mxd = {}
    for item in mantenimientos:
        if item.fecha in mxd.keys():
            # pass
            cantidad = mxd[item.fecha][0] + 1 
            mttos = mxd[item.fecha][1]
            mttos.append(item.id) 
            mxd[item.fecha] = [cantidad, mttos]
        else:
            mxd[item.fecha] = [1, [item.id]]

    # Se filtran sol los que tiene mas de un mantenimiento el mismo dia
    filtro = {}
    for item in mxd:
        if mxd[item][0]>1:
            filtro[item]=mxd[item]

    return dict(mantenimientos=mantenimientos, mxd=filtro)

def get_cliente(mantenimiento):
    contrato_mantenimiento = db.mantenimiento_contrato[mantenimiento.mantenimiento_contrato]
    cliente = db.contrato_cliente[contrato_mantenimiento.contrato]['empresa']
    return dict(cliente=cliente)

def get_users_by_group(role):
    usuarios = []
    grupo = db(db.auth_group.role == role).select().first()
    miembros = db(db.auth_membership.group_id == grupo.id).select()
    for item in miembros:
        registro = db.auth_user[item.user_id]
        usuarios.append({
            'id': registro.id,
            'username': registro.username,
            'first_name': registro.first_name,
            'last_name': registro.email,
            'email': registro.email,
        })
    return usuarios

def get_notificacion_mantenimientos_semanales():
    # Carga los manteniminetos semanales
    mantenimientos_semanales = get_mantenimiento_semanal()
    # Notifica 
    if mantenimientos_semanales:
        usuarios = get_users_by_group('Administrativo')
        usuarios.extend(get_users_by_group('Servicios'))

        for usuario in usuarios:
            for mantenimiento in mantenimientos_semanales['mantenimientos']:
                cliente = get_cliente(mantenimiento)['cliente']
                db.notificacion_sistema.validate_and_insert(
                    titulo = 'Mantenimiento Semanal',
                    mensaje = 'Esta semana, le toca mantenimiento a ' + str(cliente) + ' el ' + str((mantenimiento.fecha).strftime('%d/%m/%Y')) + '.',
                    usuario = usuario['id'],
                    estado = 'pe'
                )
    return dict()

def get_notificaciones_mantenimiento_coinciden():
    # Mantenimientos que coinciden            
    mantenimientos_mismo_dia = get_mantenimiento_mismo_dia()['mxd']
    # Notifica
    if mantenimientos_mismo_dia:
        usuarios = get_users_by_group('Servicios')
        for usuario in usuarios:
            for mantenimiento in mantenimientos_mismo_dia:
                # Selecciona el listado de los ids de los manteniminetos
                array = mantenimientos_mismo_dia[mantenimiento][1]              # [42, 55, 71, 72]
                empresas = ''
                for item in array:
                    empresas += str(get_cliente(db.mantenimiento[item])['cliente'])
                    empresas += ', '
                    


                db.notificacion_sistema.validate_and_insert(
                    titulo = 'Mantenimientos el mismo día',
                    mensaje = 'En la fecha ' + str(mantenimiento.strftime('%d/%m/%Y')) + ' coinciden ' + str(len(array)) + ' mantenimientos de las empresas: ' + str(empresas) + 'por favor revise la planificación.',
                    usuario = usuario['id'],
                    estado = 'pe'
                )

    return dict()