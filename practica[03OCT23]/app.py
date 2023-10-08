from modulo_usuarios import usuario

usuario_prueba = usuario("ricardo", "ricardo@ricardo.com")
usuario_prueba.ingresar_pass("123123")
usuario_prueba.ingresar_datos("ricardo", "biselli")
usuario_prueba.validar_credenciales("ricardo","123123")   

usuario_prueba.mostrar()