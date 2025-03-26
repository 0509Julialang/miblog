#Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#Mostrar una suma de los dos números#
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números#
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará#
#En caso de no introducir una opción válida, el programa informará de que no es correcta.#


n1 = float(input("Elegir un número principal"))
n2 = float(input("Elegir un número secundario"))

operacionmenu = float(input("Elegir un menu: menu1 - menu2 - menu3 o menu4"))

if menu1:
    print("n1 + n2")