# # Limpiando tablas principales
# db.auth_user.truncate('RESTART IDENTITY CASCADE')
# db.auth_group.truncate('RESTART IDENTITY CASCADE')
# db.auth_membership.truncate('RESTART IDENTITY CASCADE')
#
#
# # Agregando roles de usuario
# db.auth_group.validate_and_insert(role = 'Administrador', description = 'Administrador')
# db.auth_group.validate_and_insert(role = 'Administrativo', description = 'Administrativo')
# db.auth_group.validate_and_insert(role = 'Jurídico', description = 'Jurídico')
# db.auth_group.validate_and_insert(role = 'Comercial', description = 'Comercial')
# db.auth_group.validate_and_insert(role = 'Servicios', description = 'Servicios')
#
# # Agregando usuarios
# db.auth_user.validate_and_insert(first_name = 'System', last_name = 'Authority', email = 'sa@gmail.com', username = 'sa', password = 'Slallcheats*2020')
# db.auth_user.validate_and_insert(first_name = 'Administrativo', last_name = '01', email = 'administrativo01@gmail.com', username = 'administrativo01', password = 'administrativo01')
# db.auth_user.validate_and_insert(first_name = 'Jurídico', last_name = '01', email = 'juridico01@gmail.com', username = 'juridico01', password = 'juridico01')
# db.auth_user.validate_and_insert(first_name = 'Comercial', last_name = '01', email = 'comercial01@gmail.com', username = 'comercial01', password = 'comercial01')
# db.auth_user.validate_and_insert(first_name = 'Servicios', last_name = '01', email = 'servicios01@gmail.com', username = 'servicios01', password = 'servicios01')
#
# # *** Agregando usuarios de prueba ***
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '01', email = 'test01@gmail.com', username = 'test01', password = 'test01')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '02', email = 'test02@gmail.com', username = 'test02', password = 'test02')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '03', email = 'test03@gmail.com', username = 'test03', password = 'test03')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '04', email = 'test04@gmail.com', username = 'test04', password = 'test04')
#
# # Agregando permisos a los usuarios
# db.auth_membership.validate_and_insert(user_id = 1, group_id = 1)
# db.auth_membership.validate_and_insert(user_id = 2, group_id = 2)
# db.auth_membership.validate_and_insert(user_id = 3, group_id = 3)
# db.auth_membership.validate_and_insert(user_id = 4, group_id = 5)
# db.auth_membership.validate_and_insert(user_id = 5, group_id = 5)
# db.auth_membership.validate_and_insert(user_id = 6, group_id = 5)
# db.auth_membership.validate_and_insert(user_id = 7, group_id = 5)
# db.auth_membership.validate_and_insert(user_id = 8, group_id = 5)
# db.auth_membership.validate_and_insert(user_id = 9, group_id = 5)






########################################################################################################################
#                                           CARGA INICIAL DE CONTRATOS                                                 #
########################################################################################################################

# # Porveedores
#
# db.contrato_proveedor.truncate()      # >>> Limpiando tabla de contratos de proveedores
#
# # Contratacion Real Año 2022
#
# db.contrato_proveedor.validate_and_insert(anho=2022, empresa='UEB Base de Almacenes Nacionales', tipo_contrato='vt', estado_contrato='ej')
# db.contrato_proveedor.validate_and_insert(numero='CA 31/2022', anho=2022, empresa='Empresa Logística Hidráulica UEB Oriente I (Logística Hidráulica Ciego de Ávila)', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,7), fecha_vencimiento=datetime.date(2027,8,7))
# db.contrato_proveedor.validate_and_insert(numero='0680202211444794', anho=2022, empresa='Empresa de Telecomunicaciones de Cuba (ETECSA) Oficina Comercial Empresas Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,10,19), fecha_vencimiento=datetime.date(2027,10,19))
# db.contrato_proveedor.validate_and_insert(numero='0680202211444796', anho=2022, empresa='Empresa de Telecomunicaciones de Cuba (ETECSA) Oficina Comercial Empresas Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,10,19), fecha_vencimiento=datetime.date(2077,10,19))
# db.contrato_proveedor.validate_and_insert(numero='18/2022', anho=2022, empresa='TCP Alioskar Pina Mena', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,12,1), fecha_vencimiento=datetime.date(2027,12,1))
# db.contrato_proveedor.validate_and_insert(numero='99/2022', anho=2022, empresa='SURL SERVIVIP (Empresa de Servicios para el Saneamiento y la Rehabilitación Integral)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,10,5), fecha_vencimiento=datetime.date(2023,12,5))
# db.contrato_proveedor.validate_and_insert(numero='001/2022', anho=2022, empresa='SURL Qbatec', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,7,30), fecha_vencimiento=datetime.date(2025,7,30))
# db.contrato_proveedor.validate_and_insert(numero='1299754000695015', anho=2022, empresa='Banco Popular de Ahorro (BPA)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,6,28), fecha_vencimiento=datetime.date(2024,6,28))
# db.contrato_proveedor.validate_and_insert(numero='1299750000059335', anho=2022, empresa='Banco Popular de Ahorro (BPA)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,6,28), fecha_vencimiento=datetime.date(2024,6,28))
#
# # Contratacion Real Año 2023
#
# db.contrato_proveedor.validate_and_insert(numero='141/2023', anho=2023, empresa='Soluciones Tecnológicas H2A', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,6,27), fecha_vencimiento=datetime.date(2027,6,27))
# db.contrato_proveedor.validate_and_insert(numero='142/2023', anho=2023, empresa='Soluciones Tecnológicas H2A', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,6,27), fecha_vencimiento=datetime.date(2027,6,27))
# db.contrato_proveedor.validate_and_insert(numero='G MIPIME 2023', anho=2023, empresa='Empresa Comercializadora Escambray', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,6,19), fecha_vencimiento=datetime.date(2028,6,19))
# db.contrato_proveedor.validate_and_insert(numero='', anho=2023, empresa='TCP Eris Yordi Cervantes', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,6,19), fecha_vencimiento=datetime.date(2028,6,19))
# db.contrato_proveedor.validate_and_insert(numero='', anho=2023, empresa='Soluciones Tecnológicas H2A', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,1,1), fecha_vencimiento=datetime.date(2026,1,1))                                      # Ojo la fecha slo tenia el año
# db.contrato_proveedor.validate_and_insert(numero='', anho=2023, empresa='Soluciones Tecnológicas H2A', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,1,1), fecha_vencimiento=datetime.date(2026,1,1))                                      # Ojo la fecha slo tenia el año
#
# # Clientes
#
# db.contrato_cliente.truncate()      # >>> Limpiando tabla de contratos de clientes
#
# # Contratacion Real Año 2022
#
# db.contrato_cliente.validate_and_insert(numero='1', anho=2022, empresa='Empresa Provincial de Transporte Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2025,5,25))
# db.contrato_cliente.validate_and_insert(numero='2', anho=2022, empresa='UEB Mayorista 806', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2025,5,25))
# db.contrato_cliente.validate_and_insert(numero='3', anho=2022, empresa='UEB Mayorista 806', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2025,5,25))
# db.contrato_cliente.validate_and_insert(numero='4', anho=2022, empresa='UEB Transporte Agropecuario Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))
# db.contrato_cliente.validate_and_insert(numero='5', anho=2022, empresa='UEB Operación de Contenedores Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))
# db.contrato_cliente.validate_and_insert(numero='6', anho=2022, empresa='Sociedad Agroindustrial La Ceiba SRL', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))
# db.contrato_cliente.validate_and_insert(numero='7', anho=2022, empresa='Unidad Presupuestada del Gobierno Provincial Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))
# db.contrato_cliente.validate_and_insert(numero='8', anho=2022, empresa='Empresa de Energías Renovables Rensol', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))
# db.contrato_cliente.validate_and_insert(numero='9', anho=2022, empresa='UEB Ganado Menor Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,5,25), fecha_vencimiento=datetime.date(2023,5,25))                                 # Ojo la fecha se la puse yo
# db.contrato_cliente.validate_and_insert(numero='10', anho=2022, empresa='UEB EICMA Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,10), fecha_vencimiento=datetime.date(2025,8,10))
# db.contrato_cliente.validate_and_insert(numero='11', anho=2022, empresa='UEB Talleres Agropecuarios Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='13', anho=2022, empresa='Centro de Bioplantas', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='14', anho=2022, empresa='Centro de Bioplantas', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='15', anho=2022, empresa='Dirección Provincial de Justicia de Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='16', anho=2022, empresa='Dirección Provincial de Justicia de Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='17', anho=2022, empresa='EES Emp De Diseños e Ingeniera Ciego de Ávila (DIMARQ)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='18', anho=2022, empresa='EES Emp De Diseños e Ingeniera Ciego de Ávila (DIMARQ)', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='19', anho=2022, empresa='UEB Frutas Selectas Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2023,8,20))
# db.contrato_cliente.validate_and_insert(numero='20', anho=2022, empresa='UEB Frutas Selectas Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2023,8,20))
# db.contrato_cliente.validate_and_insert(numero='21', anho=2022, empresa='Dirección Provincial del Banco Popular de Ahorro (BPA)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='22', anho=2022, empresa='Dirección Provincial del Banco Popular de Ahorro (BPA)', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2022,8,20), fecha_vencimiento=datetime.date(2025,8,20))
# db.contrato_cliente.validate_and_insert(numero='22', anho=2022, empresa='Empresa Pesquera Industrial de Ciego de Ávila (EPIVILA)', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2022,10,18), fecha_vencimiento=datetime.date(2025,10,18))
#
# # Contratacion Real Año 2023
#
# db.contrato_cliente.validate_and_insert(numero='1', anho=2023, empresa='Unidad Presupuestada Del Poder Popular de Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,1,5), fecha_vencimiento=datetime.date(2026,1,1))
# db.contrato_cliente.validate_and_insert(numero='2', anho=2023, empresa='Delegacion Territorial de la Agricultura', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,4,5), fecha_vencimiento=datetime.date(2024,4,5))
# db.contrato_cliente.validate_and_insert(numero='3', anho=2023, empresa='Universidad de Ciencias Médicas', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,4,5), fecha_vencimiento=datetime.date(2024,4,5))                                     # Ojo este solo traia el nombre
# db.contrato_cliente.validate_and_insert(numero='4', anho=2023, empresa='Universidad de Ciencias Médicas', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,4,5), fecha_vencimiento=datetime.date(2024,4,5))                                     # Ojo este tambien traia solo el nombre en el registro
# db.contrato_cliente.validate_and_insert(numero='5', anho=2023, empresa='Empresa de Energias Renovables Rensol', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,2,1), fecha_vencimiento=datetime.date(2026,2,1))
# db.contrato_cliente.validate_and_insert(numero='6', anho=2023, empresa='Universidad de Ciego de Ávila "Máximo Gómez Báez"', tipo_contrato='vt', estado_contrato='ej',fecha_confeccion=datetime.date(2023,2,1), fecha_vencimiento=datetime.date(2026,2,1))                   # Ojo este viene sin fecha
# db.contrato_cliente.validate_and_insert(numero='7', anho=2023, empresa='Universidad de Ciego de Ávila "Máximo Gómez Báez"', tipo_contrato='sv', estado_contrato='ej',fecha_confeccion=datetime.date(2023,2,1), fecha_vencimiento=datetime.date(2026,2,1))                   # Ojo este viene sin fecha
#
#
# # Contratacion Real Año 2024
#
# db.contrato_cliente.validate_and_insert(numero=1, anho=2024, empresa='Hotel Meliá Cayo Coco', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,1), fecha_vencimiento=datetime.date(2025,3,1))
# db.contrato_cliente.validate_and_insert(numero=2, anho=2024, empresa='Empresa CiegoPlast', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,1), fecha_vencimiento=datetime.date(2029,3,1))
# db.contrato_cliente.validate_and_insert(numero=3, anho=2024, empresa='Empresa CiegoPlast', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,1), fecha_vencimiento=datetime.date(2029,3,1))
# db.contrato_cliente.validate_and_insert(numero=4, anho=2024, empresa='Unidad Empresarial de Base Mayorista 806', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,1), fecha_vencimiento=datetime.date(2029,3,1))
# db.contrato_cliente.validate_and_insert(numero=5, anho=2024, empresa='Unidad Empresarial de Base Mayorista 806', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,1), fecha_vencimiento=datetime.date(2029,3,1))
# db.contrato_cliente.validate_and_insert(numero=6, anho=2024, empresa='Empresa Comercial y de Servicios de Producción Universales', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,15), fecha_vencimiento=datetime.date(2029,3,15))
# db.contrato_cliente.validate_and_insert(numero=7, anho=2024, empresa='Empresa Mayorista de Productos Alimenticios y otros Bienes de Consumo', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,15), fecha_vencimiento=datetime.date(2029,3,15))
# db.contrato_cliente.validate_and_insert(numero=8, anho=2024, empresa='Empresa Mayorista de Productos Alimenticios y otros Bienes de Consumo', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,3,15), fecha_vencimiento=datetime.date(2029,3,15))
# db.contrato_cliente.validate_and_insert(numero=9, anho=2024, empresa='Productos Garriz', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=10, anho=2024, empresa='Comunales', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=11, anho=2024, empresa='Comunales', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=12, anho=2024, empresa='Logística Hidráulica Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=13, anho=2024, empresa='Logística Hidráulica Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=14, anho=2024, empresa='Empresa de Servicios Técnicos Agropecuarios Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=15, anho=2024, empresa='Empresa de Servicios Técnicos Agropecuarios Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,5,20), fecha_vencimiento=datetime.date(2029,5,20))
# db.contrato_cliente.validate_and_insert(numero=16, anho=2024, empresa='Centro de Información y Gestión Tecnológica Ciego de Ávila', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=17, anho=2024, empresa='Centro de Información y Gestión Tecnológica Ciego de Ávila', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=18, anho=2024, empresa='UEB Logística y Aseguramiento de Transporte', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=19, anho=2024, empresa='UEB Logística y Aseguramiento de Transporte', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=20, anho=2024, empresa='Universidad de Ciencias Médicas Yussef Yara', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=21, anho=2024, empresa='Universidad de Ciencias Médicas Yussef Yara', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=22, anho=2024, empresa='MIPYME Bécquer', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,6,1), fecha_vencimiento=datetime.date(2029,6,1))
# db.contrato_cliente.validate_and_insert(numero=23, anho=2024, empresa='UEB División Territorial de Comercialización de Combustible (CUPET)', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,7,29), fecha_vencimiento=datetime.date(2029,7,29))
# db.contrato_cliente.validate_and_insert(numero=24, anho=2024, empresa='UEB Mayorista de medicamentos', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,8,1), fecha_vencimiento=datetime.date(2029,8,1))
# db.contrato_cliente.validate_and_insert(numero=25, anho=2024, empresa='UEB Mayorista de medicamentos', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,8,1), fecha_vencimiento=datetime.date(2029,8,1))
# db.contrato_cliente.validate_and_insert(numero=26, anho=2024, empresa='Hotel Camino del Mar', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,11,1), fecha_vencimiento=datetime.date(2029,11,1))
# db.contrato_cliente.validate_and_insert(numero=27, anho=2024, empresa='Hotel Camino del Mar', tipo_contrato='vt', estado_contrato='ej', fecha_confeccion=datetime.date(2024,11,1), fecha_vencimiento=datetime.date(2029,11,1))
# db.contrato_cliente.validate_and_insert(numero=28, anho=2024, empresa='UEB Hotel Vigía', tipo_contrato='sv', estado_contrato='ej', fecha_confeccion=datetime.date(2024,11,1), fecha_vencimiento=datetime.date(2029,11,1))
