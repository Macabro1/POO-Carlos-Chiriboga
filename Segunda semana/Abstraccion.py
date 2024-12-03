from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

# Uso de la abstracción
perro = Perro()
perro.hacer_sonido()  # "Guau!"
gato = Gato()
gato.hacer_sonido()  # "Miau!"