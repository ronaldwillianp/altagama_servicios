# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
import uuid
import datetime

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
    # Problemas con las notificaciones cuando se conecta a BD postgres.
    # db = DAL('postgres://postgres:postgres@localhost/siged')
    # from gluon.contrib.redis_utils import RConn
    # from gluon.contrib.redis_session import RedisSession
    #
    # rconn = RConn()
    # sessiondb = RedisSession(redis_conn=rconn, session_expiry=False)
    # session.connect(request, response, db=sessiondb)

else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = []
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=True, signature=True)

# Configuracion de autenticacion
auth.settings.controller = 'usuario'
auth.settings.login_url = URL('usuario', 'iniciar_sesion')
auth.settings.login_next = URL('default', 'index')
auth.settings.on_failed_authorization = URL('usuario', 'no_autorizado')

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
# mail = auth.settings.mailer
# mail.settings.server = 'logging' if request.is_local else configuration.get(
#     'smtp.server')
# mail.settings.sender = configuration.get('smtp.sender')
# mail.settings.login = configuration.get('smtp.login')
# mail.settings.tls = configuration.get('smtp.tls') or False
# mail.settings.ssl = configuration.get('smtp.ssl') or False

# Fully configured Web2py Mailer with GMAIL
# Needed enable 2-steps authentication
# Create Password for the app in 'App Password' from Google
mail = auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'directordesarrollo.altagamasrl@gmail.com'
mail.settings.login = 'directordesarrollo.altagamasrl@gmail.com:nkpk lmjz oljr hfok '
mail.settings.tls = True
mail.settings.ssl = False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler

    scheduler = Scheduler(
        db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------
# lazy_tables = True
T.force('es')

contrato_model = db.Table(db,'contrato',
                Field('numero'),
                Field('anho'),
                Field('empresa'),
                Field('tipo_contrato'),  # Set
                Field('estado_contrato'),  # Set
                Field('fecha_vencimiento', 'date', default=lambda: (datetime.date.today()+datetime.timedelta(days=365*5))),
                Field('contrato_file', 'upload', autodelete=True),
                auth.signature,
                format='%(numero)s %(empresa)s'
)

# Validadores para Contrato
contrato_model.numero.requires = IS_INT_IN_RANGE(1, 121)
contrato_model.empresa.requires = IS_NOT_EMPTY()
contrato_model.anho.requires = IS_IN_SET(ANHOS_CONTRATO, zero=None)
contrato_model.tipo_contrato.requires = IS_IN_SET(TIPO_CONTRATO, zero=None)
contrato_model.estado_contrato.requires = IS_IN_SET(ESTADO_CONTRATO, zero=None)
contrato_model.fecha_vencimiento.requires = IS_DATE_IN_RANGE(format=T('%Y-%m-%d'), minimum=datetime.date.today())
contrato_model.contrato_file.requires = IS_EMPTY_OR(IS_FILE(extension='pdf'))

# Corrigiendo widgets
# db.contrato.numero.widget = lambda field, value: SQLFORM.widgets.string.widget(field, value, _class='form-control', _type='text', _placeholder='01/2020')

db.define_table('contrato_proveedor',
                contrato_model
)

db.define_table('contrato_cliente',
                contrato_model
)




# db.define_table('contacto',
#                 Field('nombre'),
#                 Field('cargo'),
#                 Field('tipo'),  # Set
#                 Field('numero'),
#                 Field('contrato', 'reference contrato')
# )

# db.contacto.nombre.requires = IS_NOT_EMPTY()
# db.contacto.tipo.requires = IS_IN_SET(TIPO_CONTACTO, zero=None)
# db.contacto.numero.requires = [IS_LENGTH(8, minsize=8), IS_MATCH('^\d+$', error_message='Número telefónico no válido')]
# db.contacto.contrato.requires = IS_IN_DB(db, 'contrato.numero')

# db.define_table('firma_autorizada',
#                 Field('nombre_completo'),
#                 Field('cargo'),
#                 Field('contrato', 'reference contrato'),
# )
# db.firma_autorizada.nombre_completo.requires = IS_NOT_EMPTY()
# db.firma_autorizada.contrato.requires = IS_IN_DB(db, 'contrato.numero')



# db.define_table('mantenimiento_contrato',
#                 Field('planificacion'), # Set
#                 Field('contrato', 'reference contrato'),
# )
# db.mantenimiento_contrato.planificacion.requires = IS_IN_SET(PLANIFICACION_MANTENIMIENTO, zero=None)

# db.define_table('mantenimiento',
#                 Field('mantenimiento_contrato', 'reference mantenimiento_contrato'),
#                 Field('cantidad_pc', 'integer'),
#                 Field('observaciones', 'text'),
#                 Field('fecha', 'date', default=datetime.date.today()),
#                 auth.signature
# )

# db.define_table('notificacion',
#                 Field('mensaje'),
#                 Field('grupo'),
# )






if not auth:
    redirect(URL('default', 'user/login'))
# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
