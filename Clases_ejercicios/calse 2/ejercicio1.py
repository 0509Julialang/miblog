#crear 2 listas con lo que quieras
# lista 1 el int 456789 y el str hola mundo
# luego a la lista 2 srt hola y adios luego el int 555
#lista 3 sin considerar con todo lista 1 sin considerar el ultimo elemento
#lista 4 todos los del 2 sin el primero y el ultimo
#lista 5 lista 4 mas lista 3

#decalracion de datos
lista_1 = ["mi misión", "es ayudar" "al mundo"]
lista_2 = ["ojalá", "que llueva", "cafe"]

#proceso
lista_1.append (int("45678"))
lista_1.append ("hola mundo")
lista_2.append (str("hola adios"))
lista_2.append (int("555"))

lista_3 = lista_1 [:-1]
lista_4 = lista_2 [1:-1]
lista_5 = [*lista_3, *lista_4]


#salida
#print (lista_1)
#print (lista_2)
#print (lista_3)
#print (lista_4)
print (lista_5)