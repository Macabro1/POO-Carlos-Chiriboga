class Clima:
    def __init__(self):
        # Inicializamos la lista de temperaturas como vacía
        self.temperaturas = []

    def ingresar_temperaturas(self):
        # Pedimos al usuario que ingrese las temperaturas para 7 días
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")

    def calcular_promedio(self):
        # Calculamos el promedio de las temperaturas
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        # Mostramos el promedio calculado
        promedio = self.calcular_promedio()
        print(f"\nEl promedio de temperaturas de la semana es: {promedio:.2f}°C")


# Función principal para manejar la ejecución del programa
def main():
    print("Bienvenido al programa orientado a objetos para calcular el promedio semanal del clima.")
    clima = Clima()  # Creamos una instancia de la clase Clima
    clima.ingresar_temperaturas()  # Llamamos al método para ingresar las temperaturas
    clima.mostrar_promedio()  # Mostramos el promedio


# Ejecutar el programa
if __name__ == "__main__":
    main()