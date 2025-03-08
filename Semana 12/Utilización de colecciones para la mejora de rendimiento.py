class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (autor, titulo)  # Tupla inmutable para autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[1]} por {self.datos[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios
        self.historial_prestamos = []  # Historial de préstamos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.datos[1]}' añadido correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro '{eliminado.datos[1]}' eliminado correctamente.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros and usuario.id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.datos[1]}' prestado a {usuario.nombre}.")
        else:
            print("Libro no disponible o usuario no registrado.")

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # Aseguramos que el libro se reintroduzca en la biblioteca con su ISBN
                print(f"Libro '{libro.datos[1]}' devuelto correctamente.")
                return
        print("El usuario no tiene este libro prestado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if (
                (criterios.get('titulo') and criterios['titulo'] == libro.datos[1]) or
                (criterios.get('autor') and criterios['autor'] == libro.datos[0]) or
                (criterios.get('categoria') and criterios['categoria'] == libro.categoria)
            ):
                resultados.append(libro)
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con esos criterios.")

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
if __name__ == '__main__':
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción", "12345")
    libro2 = Libro("1984", "George Orwell", "Distopía", "67890")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Crear y registrar usuario
    usuario1 = Usuario("Carlos", "U001")
    biblioteca.registrar_usuario(usuario1)

    # Prestar y devolver libro
    biblioteca.prestar_libro("12345", usuario1)
    biblioteca.listar_libros_prestados(usuario1)
    biblioteca.devolver_libro("12345", usuario1)
    biblioteca.listar_libros_prestados(usuario1)

    # Buscar libros
    biblioteca.buscar_libro(titulo="1984")