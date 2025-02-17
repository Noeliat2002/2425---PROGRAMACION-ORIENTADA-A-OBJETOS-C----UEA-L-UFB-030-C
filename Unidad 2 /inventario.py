class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def __str__(self):
        """Representación en cadena del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    """
    Clase que maneja el inventario de productos.
    """
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario, si no existe un producto con el mismo ID."""
        if id_producto not in self.productos:
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            self.productos[id_producto] = nuevo_producto
            print(f"Producto '{nombre}' agregado con éxito.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID si existe en el inventario."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o precio de un producto, según lo indicado."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.actualizar_precio(nuevo_precio)
            print(f"Producto con ID {id_producto} actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre y devuelve una lista de coincidencias."""
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


def mostrar_menu():
    """
    Muestra el menú principal en consola y permite al usuario interactuar con el sistema.
    """
    inventario = Inventario()

    while True:
        print("\n===== Sistema de Gestión de Inventarios =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario completo")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: $"))
                inventario.agregar_producto(id_producto, nombre, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores válidos.")

        elif opcion == '2':
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == '3':
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad = input("Ingrese la nueva cantidad (o deje en blanco para no cambiar): ")
                nuevo_precio = input("Ingrese el nuevo precio (o deje en blanco para no cambiar): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Ingrese valores válidos.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            if productos_encontrados:
                print(f"\nProductos encontrados con el nombre '{nombre}':")
                for producto in productos_encontrados:
                    print(producto)
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        elif opcion == '5':
            print("\nInventario completo:")
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
