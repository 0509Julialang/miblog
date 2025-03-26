# Declaración de datos
peso_nota1final = 20
peso_nota2final = 30
peso_nota3final = 50
peso_final = "peso_nota1final + peso_nota2final + peso_nota3final"

# input
nota1 = float(input("¿Cuanto te sacaste en el primer trabajo?"))
nota2 = float(input("¿y en el segundo trabajo?"))
nota3 = float(input("¿y en el tercero?"))

# proceso
notafinal = (
    (nota1 / 100 * peso_nota1final)
    + (nota2 / 100 * peso_nota2final)
    + (nota3  / 100 * peso_nota3final)
)

print(f"entonces tu nota final es:{notafinal}")
