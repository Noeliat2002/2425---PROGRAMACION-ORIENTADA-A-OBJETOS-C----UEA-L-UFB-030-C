import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        # Aquí formateo la cadena para mostrar la información del producto
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        # Intento cargar el inventario desde el archivo al iniciar
        self.cargar_inventario()
    
    def cargar_inventario(self):
        try:
            # Aquí trato de abrir el archivo y leer su contenido
            with open(self.archivo, 'r') as f:
                lineas = f.readlines()
                for linea in lineas:
                    # Cada línea tiene un producto, lo convierto a objeto Producto
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos.append(Producto(nombre, int(cantidad), float(precio)))
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError:
            # Si el archivo no existe, lo creo y continúo
            print(f"El archivo {self.archivo} no se encontró, se creará uno nuevo.")
            self.crear_archivo()
        except Exception as e:
            # Si ocurre algún otro error, lo manejo aquí
            print(f"Ocurrió un error al cargar el inventario: {e}")

    def crear_archivo(self):
        try:
            # Si no existe el archivo, lo creo vacío
            with open(self.archivo, 'w') as f:
                pass
            print(f"Archivo {self.archivo} creado exitosamente.")
        except PermissionError:
            # Si no tengo permisos, manejo el error aquí
            print(f"No tengo permisos para crear el archivo {self.archivo}.")
        except Exception as e:
            # Cualquier otro error lo manejo aquí
            print(f"Error al crear el archivo: {e}")
    
    def guardar_inventario(self):
        try:
            # Aquí guardo los productos en el archivo
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            # Si no tengo permisos para escribir en el archivo
            print(f"No tengo permisos para guardar en el archivo {self.archivo}.")
        except Exception as e:
            # Si ocurre cualquier otro error
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        # Creo un nuevo producto y lo añado a la lista
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        # Luego, guardo los cambios en el archivo
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        # Busco el producto a eliminar por nombre
        producto_eliminado = None
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                producto_eliminado = producto
                break
        # Si encontré el producto, lo elimino y guardo los cambios
        if producto_eliminado:
            self.guardar_inventario()
            print(f"Producto {producto_eliminado.nombre} eliminado exitosamente.")
        else:
            print(f"Producto con nombre {nombre} no encontrado.")
    
    def actualizar_producto(self, nombre, nueva_cantidad, nuevo_precio):
        # Busco el producto que quiero actualizar
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                self.guardar_inventario()
                print(f"Producto {nombre} actualizado exitosamente.")
                return
        print(f"Producto con nombre {nombre} no encontrado.")

    def mostrar_inventario(self):
        # Imprimo los productos en el inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Mostrar Inventario")
    print("2. Agregar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Producto")
    print("5. Salir")

def main():
    # Creo un objeto de Inventario
    inventario = Inventario()
    
    while True:
        # Muestra el menú y lee la opción del usuario
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            inventario.mostrar_inventario()
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == '3':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '4':
            nombre = input("Nombre del producto a actualizar: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, nueva_cantidad, nuevo_precio)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
