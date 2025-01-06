# Este programa calcula el área de diferentes figuras geométricas (círculo, cuadrado, rectángulo)
# y permite convertir unidades de medida (de centímetros a metros).

import math


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    # La fórmula para el área de un círculo es pi * radio^2
    area = math.pi * radio ** 2
    return area


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    # La fórmula para el área de un cuadrado es lado^2
    area = lado ** 2
    return area


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    # La fórmula para el área de un rectángulo es base * altura
    area = base * altura
    return area


# Función para convertir de centímetros a metros
def convertir_centimetros_a_metros(valor_cm):
    # 1 metro = 100 centímetros
    valor_metros = valor_cm / 100
    return valor_metros


# Función principal que ejecuta el programa
def ejecutar_programa():
    print("Bienvenido al programa de cálculo de áreas y conversión de unidades.")

    # Preguntar al usuario qué figura desea calcular
    figura = input("¿De qué figura deseas calcular el área? (círculo, cuadrado, rectángulo): ").lower()

    if figura == "círculo":
        radio = float(input("Ingresa el radio del círculo en centímetros: "))
        area_circulo = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area_circulo:.2f} cm²")
        # Convertir el área a metros cuadrados
        area_metros_circulo = convertir_centimetros_a_metros(area_circulo)
        print(f"El área del círculo en metros cuadrados es: {area_metros_circulo:.4f} m²")

    elif figura == "cuadrado":
        lado = float(input("Ingresa el lado del cuadrado en centímetros: "))
        area_cuadrado = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area_cuadrado:.2f} cm²")
        # Convertir el área a metros cuadrados
        area_metros_cuadrado = convertir_centimetros_a_metros(area_cuadrado)
        print(f"El área del cuadrado en metros cuadrados es: {area_metros_cuadrado:.4f} m²")

    elif figura == "rectángulo":
        base = float(input("Ingresa la base del rectángulo en centímetros: "))
        altura = float(input("Ingresa la altura del rectángulo en centímetros: "))
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area_rectangulo:.2f} cm²")
        # Convertir el área a metros cuadrados
        area_metros_rectangulo = convertir_centimetros_a_metros(area_rectangulo)
        print(f"El área del rectángulo en metros cuadrados es: {area_metros_rectangulo:.4f} m²")

    else:
        print("Figura no reconocida. Por favor elige entre círculo, cuadrado o rectángulo.")


# Llamada a la función principal
if __name__ == "__main__":
    ejecutar_programa()