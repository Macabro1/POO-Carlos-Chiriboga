class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

# Polimorfismo en acción
def hacer_sonido_de_animal(animal: Animal):
    animal.hacer_sonido()

perro = Perro()
gato = Gato()

hacer_sonido_de_animal(perro)  # "Guau!"
hacer_sonido_de_animal(gato)   # "Miau!"