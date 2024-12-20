# # Limpiando tablas principales
if db(db.auth_user).count()==0:
    db.auth_user.truncate()
    db.auth_group.truncate()
    db.auth_membership.truncate()


# # Agregando roles de usuario
    db.auth_group.validate_and_insert(role = 'Administrador', description = 'Administrador')
    db.auth_group.validate_and_insert(role = 'Administrativo', description = 'Administrativo')
    db.auth_group.validate_and_insert(role = 'Jurídico', description = 'Jurídico')
    db.auth_group.validate_and_insert(role = 'Comercial', description = 'Comercial')
    db.auth_group.validate_and_insert(role = 'Servicios', description = 'Servicios')

# # Agregando usuarios
    db.auth_user.validate_and_insert(first_name = 'System', last_name = 'Authority', email = 'sa@gmail.com', username = 'sa', password = 'Slallcheats*2020')
    db.auth_user.validate_and_insert(first_name = 'Administrativo', last_name = '01', email = 'administrativo01@gmail.com', username = 'administrativo01', password = 'administrativo01')
    db.auth_user.validate_and_insert(first_name = 'Jurídico', last_name = '01', email = 'juridico01@gmail.com', username = 'juridico01', password = 'juridico01')
    db.auth_user.validate_and_insert(first_name = 'Comercial', last_name = '01', email = 'comercial01@gmail.com', username = 'comercial01', password = 'comercial01')
    db.auth_user.validate_and_insert(first_name = 'Servicios', last_name = '01', email = 'servicios01@gmail.com', username = 'servicios01', password = 'servicios01')

# # *** Agregando usuarios de prueba ***
    db.auth_user.validate_and_insert(first_name = 'Test', last_name = '01', email = 'test01@gmail.com', username = 'test01', password = 'test01')
    db.auth_user.validate_and_insert(first_name = 'Test', last_name = '02', email = 'test02@gmail.com', username = 'test02', password = 'test02')
    db.auth_user.validate_and_insert(first_name = 'Test', last_name = '03', email = 'test03@gmail.com', username = 'test03', password = 'test03')
    db.auth_user.validate_and_insert(first_name = 'Test', last_name = '04', email = 'test04@gmail.com', username = 'test04', password = 'test04')

# # Agregando permisos a los usuarios
    db.auth_membership.validate_and_insert(user_id = 1, group_id = 1)
    db.auth_membership.validate_and_insert(user_id = 2, group_id = 2)
    db.auth_membership.validate_and_insert(user_id = 3, group_id = 3)
    db.auth_membership.validate_and_insert(user_id = 4, group_id = 5)
    db.auth_membership.validate_and_insert(user_id = 5, group_id = 5)
    db.auth_membership.validate_and_insert(user_id = 6, group_id = 5)
    db.auth_membership.validate_and_insert(user_id = 7, group_id = 5)
    db.auth_membership.validate_and_insert(user_id = 8, group_id = 5)
    db.auth_membership.validate_and_insert(user_id = 9, group_id = 5)

    # db.notificacion.truncate()
    db.mantenimiento.truncate()
    db.mantenimiento_contrato.truncate()
    db.firma_autorizada.truncate()
    db.contacto.truncate()
    # db.contrato.truncate()

# Contratacion Real 2024
    db.contrato_cliente.truncate()
    db.contrato_cliente.validate_and_insert(numero=1, anho=2024, empresa='Hotel Meliá Cayo Coco', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=2, anho=2024, empresa='Empresa CiegoPlast', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=3, anho=2024, empresa='Empresa CiegoPlast', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=4, anho=2024, empresa='Unidad Empresarial de Base Mayorista 806', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=5, anho=2024, empresa='Unidad Empresarial de Base Mayorista 806', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=6, anho=2024, empresa='Empresa Comercial y de Servicios de Producción Universales', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=7, anho=2024, empresa='Empresa Mayorista de Productos Alimenticios y otros Bienes de Consumo', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=8, anho=2024, empresa='Empresa Mayorista de Productos Alimenticios y otros Bienes de Consumo', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=9, anho=2024, empresa='Productos Garriz', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=10, anho=2024, empresa='Comunales', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=11, anho=2024, empresa='Comunales', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=12, anho=2024, empresa='Logística Hidráulica Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=13, anho=2024, empresa='Logística Hidráulica Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=14, anho=2024, empresa='Empresa de Servicios Técnicos Agropecuarios Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=15, anho=2024, empresa='Empresa de Servicios Técnicos Agropecuarios Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=16, anho=2024, empresa='Centro de Información y Gestión Tecnológica Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=17, anho=2024, empresa='Centro de Información y Gestión Tecnológica Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=18, anho=2024, empresa='UEB Logística y Aseguramiento de Transporte', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=19, anho=2024, empresa='UEB Logística y Aseguramiento de Transporte', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=20, anho=2024, empresa='Universidad de Ciencias Médicas Yussef Yara', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=21, anho=2024, empresa='Universidad de Ciencias Médicas Yussef Yara', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=22, anho=2024, empresa='MIPYME Bécquer', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=23, anho=2024, empresa='UEB División Territorial de Comercialización de Combustible', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=24, anho=2024, empresa='UEB Mayorista de medicamentos', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=25, anho=2024, empresa='UEB Mayorista de medicamentos', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=26, anho=2024, empresa='Hotel Caminos del Mar', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=27, anho=2024, empresa='Hotel Caminos del Mar', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))
    db.contrato_cliente.validate_and_insert(numero=28, anho=2024, empresa='UEB Hotel Vigía', tipo_contrato='sv', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))

    db.contrato_proveedor.truncate()
    db.contrato_proveedor.validate_and_insert(numero=1, anho=2024, empresa='Logística Hidráulica Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_vencimiento=(datetime.date.today()+datetime.timedelta(days=365*5)))

