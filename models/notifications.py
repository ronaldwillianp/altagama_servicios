import datetime


# Notificaciones
NOTIFICACIONES = []

try:
    NOTIFICACIONES = db(
        (db.notificacion_sistema.usuario == auth.user.id) &
        (db.notificacion_sistema.estado == 'pe')
        ).select()
except:
    pass

# NOTIFICACIONES=False

# REPORTES_PENDIENTES=[]

# CURRENT_DATE=datetime.datetime.now()

# REPORTES_VENCIDOS=[]

# if REPORTES_PENDIENTES:
    
#     for reporte in REPORTES_PENDIENTES:
        
#         if int(reporte.created_on.date().strftime("%w"))>2:
#             fecha_expiracion=reporte.created_on+datetime.timedelta(days=5)
            
#             if fecha_expiracion.date()<CURRENT_DATE.date():
#                 REPORTES_VENCIDOS.append(reporte)
#         else:
#             fecha_expiracion=reporte.created_on+datetime.timedelta(days=3)
            
#             if fecha_expiracion.date()<CURRENT_DATE.date():
                
#                 REPORTES_VENCIDOS.append(reporte)
            

#     NOTIFICACIONES=True

# def expired_since(datetime):
#     since=CURRENT_DATE-datetime
#     since=since.days
#     return since

