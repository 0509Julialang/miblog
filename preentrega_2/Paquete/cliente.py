class Cliente:
    tienda = "Mitienditaonline"

    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.compras = [] 

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

    def realizar_compra(self, producto):
        self.compras.append(producto)
        print(f"{self.nombre} compró {producto}.")

    def mostrar_compras(self):
        if self.compras:
            print(f"Compras de {self.nombre}:")
            for producto in self.compras:
                print(f"- {producto}")
        else:
            print(f"{self.nombre} no hizo ninguna compra.")