# Clase base
class Animal:
    # Atributos privados (encapsulación)
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # Métodos públicos para acceder a los atributos privados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def hacer_sonido(self):
        # Método que puede ser sobrescrito en las clases derivadas
        return "El animal hace un sonido"


# Clase derivada (herencia)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        return "El perro ladra"

    # Método adicional para la clase Perro
    def obtener_raza(self):
        return self.raza


# Clase derivada (herencia)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        return "El gato maulla"

    # Método adicional para la clase Gato
    def obtener_color(self):
        return self.color


# Crear instancias de las clases
animal_generico = Animal("Animal genérico", 5)
perro = Perro("Rex", 3, "Pastor Alemán")
gato = Gato("Felix", 2, "Gris")

# Demostrando el uso de los métodos
print(
    f"{animal_generico.obtener_nombre()} de {animal_generico.obtener_edad()} años dice: {animal_generico.hacer_sonido()}")
print(
    f"{perro.obtener_nombre()} de {perro.obtener_edad()} años, raza {perro.obtener_raza()}, dice: {perro.hacer_sonido()}")
print(
    f"{gato.obtener_nombre()} de {gato.obtener_edad()} años, color {gato.obtener_color()}, dice: {gato.hacer_sonido()}")