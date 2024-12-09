# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    print("Bienvenido al programa para calcular el promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio de temperaturas de la semana es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()