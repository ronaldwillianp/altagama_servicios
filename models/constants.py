import datetime

TIPO_CONTRATO = {
    'sv': 'Servicios',
    'vt': 'Venta'
}

ESTADO_CONTRATO = {
    'ec': 'Entregado',
    'ee': 'Recogido',
    'ej': 'Ejecución',
    'ar': 'Archivado'
}

ANHOS_CONTRATO = [
    '2020',
    '2021',
    '2022',
    '2023',
    '2024',
    '2025',
]

TIPO_CONTACTO = {
    'co': 'Corporativo',
    'pv': 'Privado',
    'fi': 'Fijo',
    'ot': 'Otros'
}


PLANIFICACION_MANTENIMIENTO = {
        'me': 'Mensual',
        'tr': 'Trimestral',
        'se': 'Semestral',
        'an': 'Anual',
}

ESTADO_MANTENIMIENTO = {
        'pl': 'Planificado',          
        'ca': 'Cancelado',
        'ej': 'Ejecutado',
}

ESTADO_NOTIFICACION = {
    'pe': 'Pendiente',
    'vi': 'Visto'
}

NOTIFICACION_MODULO = {
    'co': 'Contratos',
    'ma': 'Mantenimientos',
}

def get_current_year():
    return datetime.datetime.now().year