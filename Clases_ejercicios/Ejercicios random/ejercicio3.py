# Ingreso de datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
# Operaciones
validar_nombre = nombre != "****"
validar_nombre_longitud = len(nombre) >= 4 and len(nombre) < 8
validar_edad = edad > 5 and edad < 20
validar_edad_operacion = (edad * 3) > 35
validacion = validar_nombre and validar_nombre_longitud and validar_edad and validar_edad_operacion
# Salida
print(validacion)
