import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad en stock
        :param precio: Precio unitario
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        """Convierte el producto en una cadena de texto para guardar en el archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data):
        """Convierte una cadena de texto en un objeto Producto."""
        partes = data.strip().split(",")
        return Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """Constructor de la clase Inventario, inicializa una lista vacía de productos."""
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo."""
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo, "r") as f:
                for line in f:
                    producto = Producto.from_string(line)
                    self.productos.append(producto)
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el archivo: {e}")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(producto.to_dict() + "\n")
            print("Inventario guardado correctamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto si el ID es único."""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o precio de un producto por ID."""
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (puede haber nombres similares)."""
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIOS ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# Ejecutar el menú si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
