# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----

@auth.requires_login()
def index():
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
