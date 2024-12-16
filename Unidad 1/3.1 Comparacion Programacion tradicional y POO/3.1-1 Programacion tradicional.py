# Función para ingresar las temperaturas
def ingresar_temperaturas():
    # Lista donde voy a guardar las temperaturas
    temperaturas = []
    for i in range(7):  # Como son 7 días, hago un ciclo de 7 veces
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Pido la temperatura de cada día
        temperaturas.append(temp)  # Añado la temperatura a la lista
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    # Sumo todas las temperaturas y las divido por la cantidad de días (7)
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal que organiza el flujo
def main():
    # Primero pido las temperaturas
    temperaturas = ingresar_temperaturas()
    
    # Después calculo el promedio
    promedio = calcular_promedio(temperaturas)
    
    # Imprimo el resultado
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Llamo a la función principal para que el programa empiece
if __name__ == "__main__":
    main()
