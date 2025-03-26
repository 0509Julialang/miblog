usuarios= []

def registrarse():
    nombre_usuario = input("Cree un nombre de usuario: ")
    while True:
        contraseña = input("Cree una contraseña (debe tener entre 5 y 10 caracteres): ")
        if len(contraseña) in range(5, 11):
            return {"username": nombre_usuario, "password": contraseña}
        else:
            print("La contraseña debe tener entre 5 y 10 caracteres. Inténtelo de nuevo.")

def login():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario["username"] == nombre_usuario and usuario["password"] == contraseña:
            return True
    return False

def main():
    while True:
        print("\n Bienvenido/a a su cuenta: a continuación encontrará el menú de opciones")
        print("1. Registrarse")
        print("2. Logearse")
        print("3. Salir")
        print("4. Ver base de datos de usuarios")

        
        opción = input("Seleccione una opción: ")
        if opción == "1":
            usuario = registrarse()
            usuarios.append(usuario)
            print("Registro exitoso")
            print("Por favor inicie sesión con su cuenta")
            if login():
                print("Inicio de sesión exitoso")
            else:
                print("Nombre de usuario o contraseña incorrecto.")
        elif opción == "2":
            if login():
                print("Inicio de sesión exitoso")
            else:
                print("Nombre de usuario o contraseña incorrecto.")
        elif opción == "4":
            if usuarios:
                print("Listado de usuarios registrados:")
                for usuario in usuarios:
                    print(f"Usuario: {usuario['username']}, Contraseña: {usuario['password']}")
            else:
                print("No hay usuarios registrados.")
        elif opción == "3":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

main()