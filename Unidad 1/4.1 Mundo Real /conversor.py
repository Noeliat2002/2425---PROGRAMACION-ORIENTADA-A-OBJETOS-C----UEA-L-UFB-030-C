# Función para convertir metros a otras unidades
def convertir_metros_a_unidades(metros):
    kilometros = metros / 1000.0  # Conversión de metros a kilómetros
    centimetros = metros * 100.0  # Conversión de metros a centímetros
    milimetros = metros * 1000.0  # Conversión de metros a milímetros
    return kilometros, centimetros, milimetros

# Función para imprimir los resultados
def imprimir_resultados(metros, kilometros, centimetros, milimetros):
    print(f"\n{metros} metros equivalen a:")
    print(f"{kilometros:.3f} kilómetros")
    print(f"{centimetros} centímetros")
    print(f"{milimetros} milímetros")

# Función principal para interactuar con el usuario
def ejecutar_programa():
    continuar = True

    while continuar:
        # Solicitar entrada del usuario y convertir a float
        metros = float(input("Ingresa la cantidad de metros: "))

        # Obtener conversiones
        kilometros, centimetros, milimetros = convertir_metros_a_unidades(metros)

        # Mostrar los resultados
        imprimir_resultados(metros, kilometros, centimetros, milimetros)

        # Preguntar si el usuario desea continuar
        respuesta = input("\n¿Deseas hacer otra conversión? (s/n): ")
        if respuesta.lower() != 's':
            continuar = False
            print("Gracias por usar el conversor de unidades.")

if __name__ == "__main__":
    ejecutar_programa()
