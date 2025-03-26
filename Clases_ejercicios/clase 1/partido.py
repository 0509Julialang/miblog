#calcular el promedio final de los equipos de futbol en un torneo, 
# Jugaron 20 partidos, 
# partidos ganados 3 puntos, 
# partido empatado 1 punto, 
# partido perdido 0 punto 
# cantidad de puntos dividido, cantidad de partidos

#declaracion de valores
cantidad_de_partidos = 20
puntos_ganados = 3
puntos_empatados = 1
puntos_perdidos = 0

#imput
total_partidos_ganados = float(input("¿cuantos partidos ganaste?"))
total_partidos_empatados = float(input("¿cuantos partidos empataste?"))
total_partidos_perdidos = float(input("¿cuantos partidos perdiste?"))

#operacion
total_puntos = float(total_partidos_ganados * puntos_ganados) + (total_partidos_empatados * puntos_empatados) + (total_partidos_perdidos *puntos_perdidos)
print(f"entonces tu puntaje final es:{total_puntos}")