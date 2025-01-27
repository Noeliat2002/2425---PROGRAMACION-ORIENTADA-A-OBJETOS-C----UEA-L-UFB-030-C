# Definición de la clase "Estudiante"
class Estudiante:
    # El constructor (__init__) se usa para inicializar los datos del estudiante
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        # Imprimo un mensaje cuando el estudiante se crea
        print(f"Se ha creado el estudiante {self.nombre}, de {self.edad} años, estudiando {self.carrera}.")
    
    # El destructor (__del__) se invoca cuando el objeto se destruye
    def __del__(self):
        # Al eliminar el objeto, imprimo un mensaje
        print(f"El estudiante {self.nombre} ha terminado su curso y ha sido eliminado.")
    
    # Método para mostrar la información del estudiante
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}")

# En el bloque principal del programa se crean los objetos de la clase Estudiante
if __name__ == "__main__":
    # Creo dos objetos de la clase Estudiante con diferentes atributos
    estudiante1 = Estudiante("Juan Pérez", 20, "Ingeniería en Sistemas")
    estudiante2 = Estudiante("María López", 22, "Arquitectura")
    
    # Llamo al método para mostrar la información de cada estudiante
    estudiante1.mostrar_info()
    estudiante2.mostrar_info()

    # Elimino los objetos explícitamente para ver cómo se llama el destructor
    del estudiante1
    del estudiante2
