# main.py

from Paquete.cliente import Cliente

def main():
    cliente1 = Cliente("Julia Langoni", "julia.langoni@gmail.com", "Calle 37 n°811", "2215039940")

    # Info cliente
    print(cliente1)

    # Realiza compras
    cliente1.realizar_compra("Celular")
    cliente1.realizar_compra("Cámara de fotos")

    # Mostrar compras realizadas
    cliente1.mostrar_compras()

if __name__ == "__main__":
    main()