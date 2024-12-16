# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de un coche

class Coche:
    def __init__(self, rendimiento_combustible=25):
        self.capacidad_tanque = 0
        self.distancia_recorrida = 0
        self.rendimiento_combustible = rendimiento_combustible

    def cargar_tanque(self, cantidad):
        self.capacidad_tanque += cantidad

    def viajar(self, distancia):
        combustible_requerido = distancia / self.rendimiento_combustible
        if combustible_requerido <= self.capacidad_tanque:
            self.capacidad_tanque -= combustible_requerido
            self.distancia_recorrida += distancia
            print("Viajando:", distancia, "kilómetros")
        else:
            print("No tienes suficiente combustible para esa distancia.")

# Crear una instancia de la clase Coche
vehiculo = Coche()

# Uso de los métodos en la programación orientada a objetos
vehiculo.cargar_tanque(20)
vehiculo.viajar(100)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Distancia recorrida (POO):", vehiculo.distancia_recorrida)
print("Capacidad del tanque (POO):", vehiculo.capacidad_tanque)
