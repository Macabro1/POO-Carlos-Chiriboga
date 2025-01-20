# Clase que simula la gestión de un archivo
class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase. Se llama cuando se crea un nuevo objeto de la clase.
        Inicializa el atributo 'nombre_archivo' y simula la apertura de un archivo.
        """
        self.nombre_archivo = nombre_archivo  # Asigna el nombre del archivo
        self.archivo = open(nombre_archivo, 'w')  # Abre el archivo en modo escritura
        print(f"Archivo '{self.nombre_archivo}' ha sido abierto para escritura.")

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo.
        Este método recibe el contenido y lo escribe en el archivo.
        """
        self.archivo.write(contenido)  # Escribe el contenido en el archivo
        print(f"Se ha escrito en el archivo: {contenido}")

    def __del__(self):
        """
        Destructor de la clase. Se llama cuando el objeto es destruido (cuando el
        objeto se elimina o cuando el programa termina). Aquí se cierra el archivo
        de forma segura.
        """
        try:
            self.archivo.close()  # Cierra el archivo
            print(f"Archivo '{self.nombre_archivo}' ha sido cerrado.")
        except AttributeError:
            # Si no se había abierto un archivo, no hace nada.
            pass

# Crear un objeto de la clase Archivo y trabajar con él
def main():
    archivo_objeto = Archivo("mi_archivo.txt")  # Se crea el objeto, lo que llama a __init__
    archivo_objeto.escribir("Este es el contenido de prueba.\n")  # Escribe en el archivo

    # El objeto 'archivo_objeto' se eliminará al final de la ejecución,
    # lo que invocará automáticamente el destructor __del__.
    del archivo_objeto  # El destructor __del__ es llamado explícitamente al eliminar el objeto

# Ejecutamos la función principal
if __name__ == "__main__":
    main()