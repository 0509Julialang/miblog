#declaracion de datos
peso_nota_1 = 20
peso_nota_2 = 30
peso_nota_3 = 50
peso_total = peso_nota_1 + peso_nota_2 + peso_nota_3


#entrada
nota_1 = float(input("¿cual fue tu primer nota?"))
nota_2 = float(input("¿cual fue tu segunda nota?"))
nota_3 = float(input("¿cual fue tu tercer nota?"))

#proceso
nota_final= ((nota_1 * peso_nota_1) + (nota_2 * peso_nota_2) + (nota_3 * peso_nota_3)) / (peso_total)

#salida
print(f"tu nota final es: {nota_final}")