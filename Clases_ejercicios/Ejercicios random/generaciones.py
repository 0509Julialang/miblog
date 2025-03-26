#consigna: Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado.
#Trabajarán con el notebook de clase Clase_4.ipynb
#Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: 
# “No existe generación asociada”

generacion = int(input("¿en que fecha naciste?"))

if generacion (1920,1940)
print("Es generacion silenciosa")

elif generacion (1946,1964)
    print("Es generacion baby boomer")
    
elif generacion (1965,1979)
    print("Es generacion x")

elif generacion (1980,2000)
    print("Es generacion y")

elif generacion (2001,2010)
    print("Es generacion z")

else generacion (2010,2025 and 1920,1800)


año = int(input("Ingresa un año de nacimiento: "))
if año >= 1920 and año <= 1940:
    generacion = "Generación Silenciosa"
elif año >= 1946 and año <= 1964:
    generacion = "Baby Boomer"
elif año >= 1965 and año <= 1979:
    generacion = "Generación X"
elif año >= 1980 and año <= 2000:
    generacion = "Generación Y"
else:
    generacion = ""
if generacion:
    print(f"El año {año} corresponde a la {generacion}.")
else:
    print("No hay una generación asociada al año.")