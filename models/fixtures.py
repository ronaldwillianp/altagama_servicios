# # Limpiando tablas principales
# db.auth_user.truncate()
# db.auth_group.truncate()
# db.auth_membership.truncate()

# # Agregando roles de usuario
# db.auth_group.validate_and_insert(role = 'Administrador', description = 'Administrador')
# db.auth_group.validate_and_insert(role = 'Administrativo', description = 'Administrativo')
# db.auth_group.validate_and_insert(role = 'Jurídico', description = 'Jurídico')
# db.auth_group.validate_and_insert(role = 'Comercial', description = 'Comercial')
# db.auth_group.validate_and_insert(role = 'Servicios', description = 'Servicios')

# # Agregando usuarios
# db.auth_user.validate_and_insert(first_name = 'System', last_name = 'Authority', email = 'sa@gmail.com', username = 'sa', password = 'Slallcheats*2020')
# db.auth_user.validate_and_insert(first_name = 'Administrativo', last_name = '01', email = 'administrativo01@gmail.com', username = 'administrativo01', password = 'administrativo01')
# db.auth_user.validate_and_insert(first_name = 'Jurídico', last_name = '01', email = 'juridico01@gmail.com', username = 'juridico01', password = 'juridico01')
# db.auth_user.validate_and_insert(first_name = 'Comercial', last_name = '01', email = 'comercial01@gmail.com', username = 'comercial01', password = 'comercial01')
# db.auth_user.validate_and_insert(first_name = 'Servicios', last_name = '01', email = 'servicios01@gmail.com', username = 'servicios01', password = 'servicios01')

# # *** Agregando usuarios de prueba ***
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '01', email = 'test01@gmail.com', username = 'test01', password = 'test01')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '02', email = 'test02@gmail.com', username = 'test02', password = 'test02')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '03', email = 'test03@gmail.com', username = 'test03', password = 'test03')
# db.auth_user.validate_and_insert(first_name = 'Test', last_name = '04', email = 'test04@gmail.com', username = 'test04', password = 'test04')

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

