#Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetirse el proceso hasta que lo introduzca correctamente.

#numeroimpar = float(input("Elegir un número impar"))#

#Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100: 
# 🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
# El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
    