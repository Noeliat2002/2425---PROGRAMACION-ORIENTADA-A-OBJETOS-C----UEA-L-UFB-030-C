# Programación Tradicional
# Ejemplo: Administración de un coche

# Definición de variables globales
capacidad_tanque = 0
distancia_recorrida = 0
rendimiento_combustible = 25

# Función para cargar el tanque de combustible
def cargar_tanque(cantidad):
    global capacidad_tanque
    capacidad_tanque += cantidad

# Función para viajar con el coche
def viajar(distancia):
    global capacidad_tanque, distancia_recorrida, rendimiento_combustible
    combustible_requerido = distancia / rendimiento_combustible
    if combustible_requerido <= capacidad_tanque:
        capacidad_tanque -= combustible_requerido
        distancia_recorrida += distancia
        print("Viajando:", distancia, "kilómetros")
    else:
        print("No tienes suficiente combustible para esa distancia.")

# Uso de las funciones en la programación tradicional
cargar_tanque(20)
viajar(100)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Distancia recorrida (Tradicional):", distancia_recorrida)
print("Capacidad del tanque (Tradicional):", capacidad_tanque)
