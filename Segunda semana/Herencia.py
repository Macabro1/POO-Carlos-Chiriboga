class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la superclase
        self.puertas = puertas

    def descripcion(self):
        return f"{self.marca} {self.modelo}, {self.puertas} puertas"

# Uso de la herencia
coche = Coche("Toyota", "Corolla", 4)
print(coche.descripcion())  # "Toyota Corolla, 4 puertas"