edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad no válida")
elif edad < 13: 
    print("Eres niño.")
elif edad < 18: 
    print("Eres adolescente")
elif edad < 65: 
    print("Eres adulto joven")
else
    print("Eres adulto mayor")