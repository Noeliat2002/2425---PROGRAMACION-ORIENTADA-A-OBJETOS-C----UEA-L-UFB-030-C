# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        # Representación del producto en formato legible
        return f"{self.nombre} - ${self.precio}"

# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)

    def mostrar_carrito(self):
        if self.carrito:
            print(f"\nCarrito de {self.nombre}:")
            for producto in self.carrito:
                print(f"- {producto}")
        else:
            print(f"{self.nombre}, tu carrito está vacío.")

    def total_carrito(self):
        return sum([producto.precio for producto in self.carrito])

# Función para gestionar la tienda
def gestionar_tienda():
    # Crear algunos productos
    camiseta = Producto("Camiseta", 25)
    pantalon = Producto("Pantalón", 50)
    zapato = Producto("Zapato", 60)

    # Crear un cliente
    cliente = Cliente("Ana")

    # Simular un proceso de compra
    cliente.agregar_producto(camiseta)
    cliente.agregar_producto(pantalon)
    cliente.agregar_producto(zapato)

    # Mostrar carrito y el total
    cliente.mostrar_carrito()
    print(f"\nTotal de la compra: ${cliente.total_carrito()}")

if __name__ == "__main__":
    gestionar_tienda()
