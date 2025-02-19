# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@auth.requires_login()
def index():
    empresas_mas_mantenimientos = get_5_enterprise_mantainences()['clientes']
    empresas_menos_mantenimientos = get_inverted_5_enterprise_mantainences()['clientes']
    total_contratos_clientes = db(db.contrato_cliente.id>0).count()
    total_contratos_proveedores = db(db.contrato_proveedor.id>0).count()
    total_contratos = total_contratos_clientes + total_contratos_proveedores
    total_archivados = db(db.contrato_cliente.estado_contrato == 'ar').count() + db(db.contrato_proveedor.estado_contrato == 'ar').count()
    total_entregados = db(db.contrato_cliente.estado_contrato == 'ec').count() + db(db.contrato_proveedor.estado_contrato == 'ec').count()
    total_recogidos = db(db.contrato_cliente.estado_contrato == 'ee').count() + db(db.contrato_proveedor.estado_contrato == 'ee').count()
    total_ejecucion = db(db.contrato_cliente.estado_contrato == 'ej').count() + db(db.contrato_proveedor.estado_contrato == 'ej').count()
    total_clientes_mantenimiento = len(db(db.mantenimiento.id>0).select(orderby=db.mantenimiento.id, groupby=db.mantenimiento.contrato))
    porciento_no_archivados_total = round((total_contratos-total_archivados)*100/total_contratos, 2)
    porciento_clientes_mantenimiento = round((total_clientes_mantenimiento)*100/total_contratos_clientes, 2)
    

    ultimo_contrato_cliente_servicio = db(
        (db.contrato_cliente.id>0) &
        (db.contrato_cliente.tipo_contrato == 'sv')
    ).select(
        db.contrato_cliente.id, 
        db.contrato_cliente.numero, 
        db.contrato_cliente.anho, 
        db.contrato_cliente.empresa
    ).last()
    ultimo_contrato_cliente_venta = db(
        (db.contrato_cliente.id>0) &
        (db.contrato_cliente.tipo_contrato == 'vt')
    ).select(
        db.contrato_cliente.id, 
        db.contrato_cliente.numero, 
        db.contrato_cliente.anho, 
        db.contrato_cliente.empresa
    ).last()

    return dict(
        total_contratos_clientes = total_contratos_clientes,
        total_contratos_proveedores= total_contratos_proveedores,
        total_contratos = total_contratos,
        total_archivados = total_archivados,
        total_entregados=total_entregados,
        total_recogidos=total_recogidos,
        total_ejecucion=total_ejecucion,
        total_clientes_mantenimiento = total_clientes_mantenimiento,
        ultimo_contrato_cliente_servicio=ultimo_contrato_cliente_servicio,
        ultimo_contrato_cliente_venta = ultimo_contrato_cliente_venta,
        porciento_no_archivados_total = porciento_no_archivados_total,
        porciento_clientes_mantenimiento = porciento_clientes_mantenimiento,
        empresas_mas_mantenimientos = empresas_mas_mantenimientos,
        empresas_menos_mantenimientos = empresas_menos_mantenimientos
    )

@auth.requires_login()
def index2():
    total_contratos_clientes = db(db.contrato_cliente.id>0).count()
    total_contratos_proveedores = db(db.contrato_proveedor.id>0).count()
    total_contratos = total_contratos_clientes + total_contratos_proveedores
    total_archivados = db(db.contrato_cliente.estado_contrato == 'ar').count() + db(db.contrato_proveedor.estado_contrato == 'ar').count() 
    
    return dict(
        total_contratos_clientes = total_contratos_clientes,
        total_contratos_proveedores= total_contratos_proveedores,
        total_contratos = total_contratos,
        total_archivados = total_archivados,
    )

# ---- Embedded wiki (example) ----


def wiki():
    auth.wikimenu()  # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
