# Defino una clase llamada Clima
class Clima:
    def __init__(self):
        # Lista donde voy a guardar las temperaturas de los 7 días
        self.temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):  # Recorro 7 días
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  # Pido cada temperatura
            self.temperaturas.append(temp)  # La agrego a la lista de temperaturas

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(self.temperaturas)  # Sumo todas las temperaturas
        promedio = total / len(self.temperaturas)  # Calculo el promedio
        return promedio

# Función principal que organiza todo
def main():
    # Creo un objeto de la clase Clima
    clima = Clima()
    
    # Llamo al método de ingresar las temperaturas
    clima.ingresar_temperaturas()
    
    # Llamo al método para calcular el promedio
    promedio = clima.calcular_promedio()
    
    # Muestro el resultado
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Llamo a la función principal
if __name__ == "__main__":
    main()
