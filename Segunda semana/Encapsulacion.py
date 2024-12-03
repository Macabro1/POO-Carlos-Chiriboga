class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def obtener_nombre(self):  # Método público
        return self.__nombre

    def set_edad(self, edad):  # Método público
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad no válida")

# Uso de la clase
persona = Persona("Juan", 30)
print(persona.obtener_nombre())  # "Juan"
persona.set_edad(35)