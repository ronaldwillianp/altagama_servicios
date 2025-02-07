@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def detalles():
    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato_servicio_mantenimiento'))

    mantenimientos = db(
        db.mantenimiento.mantenimiento_contrato == db(
            db.mantenimiento_contrato.contrato == registro.id).select().first().id
    ).select(orderby=~db.mantenimiento.fecha)
    return dict(mantenimientos=mantenimientos)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def contrato_servicio_mantenimiento():
    rows = db(
        (db.contrato_cliente.id > 0) &
        (db.contrato_cliente.estado_contrato == 'ej') &
        (db.contrato_cliente.tipo_contrato == 'sv')
    ).select(
        db.contrato_cliente.id,
        db.contrato_cliente.numero,
        db.contrato_cliente.anho,
        db.contrato_cliente.empresa,
        db.mantenimiento_contrato.id,
        left=db.mantenimiento_contrato.on(db.contrato_cliente.id == db.mantenimiento_contrato.contrato)
    )
    return dict(rows=rows)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def habilitar_mantenimiento():
    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato_servicio_mantenimiento'))

    db.mantenimiento_contrato.contrato.writable = False
    form = SQLFORM(db.mantenimiento_contrato)
    form.vars.contrato = registro.id

    if form.process().accepted:
        session.status = True
        session.msg = 'Mantenimiento habilitado para este contrato'
        redirect(URL('mantenimiento', 'contrato_servicio_mantenimiento'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'
    return dict(form=form)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def deshabilitar_mantenimiento():
    registro = db.contrato_cliente(request.args(0, cast=int)) or redirect(URL('contrato_servicio_mantenimiento'))
    row = db(db.mantenimiento_contrato.contrato == registro.id).select().first()
    mantenimientos = db(db.mantenimiento.mantenimiento_contrato == row.id).count()

    if mantenimientos > 0:
        session.error = True
        session.msg = 'No es posible deshabilitar. Este contrato tiene mantenimientos.'
    else:
        db(db.mantenimiento_contrato.id == row.id).delete()
        session.status = True
        session.msg = 'Mantenimiento deshabilitado para este contrato'
    redirect(URL('mantenimiento', 'contrato_servicio_mantenimiento'))
    return dict()


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def administrar():
    # Listado de clientes de la BD que reciben servicios [Para poder asignar mantenimiento]
    clientes = db(
        (db.contrato_cliente.id > 0) &
        (db.contrato_cliente.tipo_contrato == 'sv')
    ).select()

    # Si viene alguna peticion especifica de la vista para filtrar determinados clientes
    if request.vars:
        # Las peticiones pueden ser vacias, de un elemento(str) o multiples(list)
        rows = []
        # Se evalua el tipo de peticion, en este caso si es instancia de la clase <list>
        if isinstance(request.vars['filtro'], list) :
            # Se recorren las entidades seleccionadas y se
            for i in request.vars['filtro']:
                for mantenimiento in db(db.mantenimiento.contrato == i).select():
                    rows.append(mantenimiento)
        elif type(request.vars['filtro']) == str:
            for mantenimiento in db(db.mantenimiento.contrato == request.vars['filtro']).select():
                rows.append(mantenimiento)

            for cliente in clientes:
                if cliente.id == int(request.vars['filtro']):
                    cliente['selected'] = True
                else:
                    cliente['selected'] = False
    else:
        rows = db(db.mantenimiento.id > 0).select()
        for cliente in clientes:
            cliente['selected'] = False

    return dict(rows=rows, clientes=clientes)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def preprocess_mantenimiento(form):
    # Selecciona el ultimo mantenimiento
    ultimo_mantenimiento = db(
        (db.mantenimiento.id > 0) &
        (db.mantenimiento.contrato == form.vars.contrato)
    ).select(
        orderby=~db.mantenimiento.fecha
    ).first()
    # Chequea que la fecha seleccionada sea mayor a la del ultimo mantenimiento
    if ultimo_mantenimiento:
        if ultimo_mantenimiento.fecha >= form.vars.fecha:
            form.errors.fecha = 'La fecha debe ser mayor a ' + str(ultimo_mantenimiento.fecha.strftime('%d/%m/%Y'))


def mantenimientos_pendientes(contrato):
    # Si existen mantenimientos pendientes
    mantenimientos = db(db.mantenimiento.mantenimiento_contrato == contrato).select()
    mantenimientos_pendientes = []
    for item in mantenimientos:
        if item.estado == 'pl':
            mantenimientos_pendientes.append(item)
    if mantenimientos_pendientes:
        session.error = True
        session.msg = 'Existe %s mantenimiento(s) con estado Planificado en esta empresa. No puede planificar otro hasta Ejecutar/Cancelar/Eliminar los pendientes.' % len(
            mantenimientos_pendientes)
        redirect(URL('mantenimiento', 'administrar', args=contrato.contrato))


def planificar_fecha(contrato, form):
    # Si existen al menos un mantenimiento de este contrato
    if db(db.mantenimiento.mantenimiento_contrato == contrato.id).count() > 0:
        # Seleccionamos la fecha del ultimo mantenimiento
        ultima_fecha = db(
            db.mantenimiento.mantenimiento_contrato == contrato.id).select().last().fecha_siguiente_mantenimiento

        # if contrato.planificacion == 'me':
        #     form.vars.fecha = (ultima_fecha + datetime.timedelta(days=30)).strftime('%d/%m/%Y')
        # elif contrato.planificacion == 'tr':
        #     form.vars.fecha = (ultima_fecha + datetime.timedelta(days=90)).strftime('%d/%m/%Y')
        # elif contrato.planificacion == 'se':
        #     form.vars.fecha = (ultima_fecha + datetime.timedelta(days=180)).strftime('%d/%m/%Y')
        # else:
        #     form.vars.fecha = (ultima_fecha + datetime.timedelta(days=365)).strftime('%d/%m/%Y')

        form.vars.fecha = ultima_fecha.strftime('%d/%m/%Y')


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def editar():
    if not request.args(0):
        redirect(URL('mantenimiento', 'administrar', args=request.args(0)))

    registro = db.mantenimiento(request.args(0, cast=int)) or redirect(URL('mantenimiento', 'administrar'))

    db.mantenimiento.contrato.writable = False

    if (registro.estado == 'ca') or (registro.estado == 'ej'):
        session.error = True
        session.msg = 'No se puede editar un mantenimiento ' + str(ESTADO_MANTENIMIENTO[registro.estado]).lower() + '.'
        redirect(URL('mantenimiento', 'administrar', args=request.args(1)))

    form = SQLFORM(db.mantenimiento, registro)

    if form.process().accepted:
        session.status = True
        session.msg = 'Mantenimiento actualizado correctamente'
        redirect(URL('mantenimiento', 'administrar', args=request.args(1)))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, registro=registro)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def eliminar():
    if not request.args(0):
        redirect(URL('mantenimiento', 'contrato_servicio_mantenimiento'))

    mantenimiento_contrato = None
    if session.mantenimiento_contrato:
        mantenimiento_contrato = session.mantenimiento_contrato
        del (session.mantenimiento_contrato)

    registro = db.mantenimiento(request.args(0, cast=int)
                                ) or redirect(URL('mantenimiento', 'administrar', args=mantenimiento_contrato))
    x = registro.id

    db(db.mantenimiento.id == x).delete()
    session.status = True
    session.msg = 'Mantenimiento eliminado correctamente'
    redirect(URL("mantenimiento", "administrar", args=mantenimiento_contrato))

    return dict()


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def editar_planificacion():
    if not request.args(0):
        redirect(URL('mantenimiento', 'contrato_servicio_mantenimiento', args=request.args(0)))

    contrato = db.contrato_cliente(request.args(0, cast=int)) or redirect(
        URL('mantenimiento', 'contrato_servicio_mantenimiento', args=request.args(0)))

    registro = db(db.mantenimiento_contrato.contrato == contrato.id).select().first()

    db.mantenimiento_contrato.contrato.writable = False
    form = SQLFORM(db.mantenimiento_contrato, registro)

    if form.process().accepted:
        session.status = True
        session.msg = 'Frecuencia de mantenimiento actualizada correctamente'
        redirect(URL('mantenimiento', 'contrato_servicio_mantenimiento', args=request.args(0)))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form)


def get_cliente(mantenimiento):
    contrato_mantenimiento = db.mantenimiento_contrato[mantenimiento.mantenimiento_contrato]
    cliente = db.contrato_cliente[contrato_mantenimiento.contrato]['empresa']
    return dict(cliente=cliente)


def calendario():
    mantenimientos = db(db.mantenimiento.id > 0).select()
    for item in mantenimientos:
        item['cliente'] = get_cliente(item)['cliente']
    return dict(mantenimientos=mantenimientos)


@auth.requires(
    auth.has_membership(role='Administrador') or
    auth.has_membership(role='Administrativo') or
    auth.has_membership(role='Servicios')
)
def crear():
    clientes = db(
        (db.contrato_cliente.id > 0) &
        (db.contrato_cliente.tipo_contrato == 'sv')
    ).select()

    db.mantenimiento.estado.writable = False
    form = SQLFORM(db.mantenimiento)
    form.vars.estado = 'pl'

    if form.process(onvalidation=preprocess_mantenimiento).accepted:
        session.status = True
        session.msg = 'Mantenimiento actualizado correctamente'
        redirect(URL('mantenimiento', 'administrar'))
    elif form.errors:
        session.error = True
        session.msg = 'El formulario tiene errores'

    return dict(form=form, clientes=clientes)
