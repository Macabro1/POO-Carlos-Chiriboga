# Definimos la clase "Producto" que representará los productos de la tienda.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad disponible del producto

    def actualizar_cantidad(self, cantidad_vendida):
        """Actualiza la cantidad disponible del producto después de una venta."""
        if self.cantidad >= cantidad_vendida:
            self.cantidad -= cantidad_vendida
            return True
        else:
            return False

    def __str__(self):
        """Representación del producto como una cadena de texto."""
        return f"{self.nombre} - ${self.precio} (Cantidad disponible: {self.cantidad})"


# Definimos la clase "Carrito" que representa el carrito de compras de un cliente.
class Carrito:
    def __init__(self):
        self.productos = []  # Lista de productos en el carrito

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito si hay suficiente cantidad disponible."""
        if producto.actualizar_cantidad(cantidad):
            self.productos.append({"producto": producto, "cantidad": cantidad})
            return True
        else:
            return False

    def calcular_total(self):
        """Calcula el total de la compra en el carrito."""
        total = 0
        for item in self.productos:
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_contenido(self):
        """Muestra el contenido del carrito de compras."""
        if len(self.productos) == 0:
            print("El carrito está vacío.")
        else:
            for item in self.productos:
                print(f"{item['producto'].nombre} x{item['cantidad']} - ${item['producto'].precio * item['cantidad']}")
            print(f"Total: ${self.calcular_total()}")


# Definimos la clase "Cliente" que representa a un cliente de la tienda.
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Email del cliente

    def __str__(self):
        """Representación del cliente como una cadena de texto."""
        return f"Cliente: {self.nombre} (Email: {self.email})"


# Definimos la clase "Orden" que representa una orden realizada por un cliente.
class Orden:
    def __init__(self, cliente, carrito):
        self.cliente = cliente  # Cliente que realiza la orden
        self.carrito = carrito  # Carrito con los productos de la compra
        self.total = carrito.calcular_total()  # Total de la compra

    def generar_factura(self):
        """Genera la factura con los productos y el total."""
        factura = f"Factura para {self.cliente}\n"
        factura += "-" * 30 + "\n"
        for item in self.carrito.productos:
            factura += f"{item['producto'].nombre} x{item['cantidad']} - ${item['producto'].precio * item['cantidad']}\n"
        factura += "-" * 30 + "\n"
        factura += f"Total: ${self.total}\n"
        return factura

# Crear productos
producto1 = Producto("Laptop", 1000, 5)
producto2 = Producto("Teléfono", 500, 10)
producto3 = Producto("Auriculares", 150, 20)

# Crear un cliente
cliente1 = Cliente("Carlos Chiriboga", "cm.chiribogah@uea.edu.ec")

# Crear un carrito y agregar productos
carrito_cliente1 = Carrito()
carrito_cliente1.agregar_producto(producto1, 1)  # 1 Laptop
carrito_cliente1.agregar_producto(producto2, 2)  # 2 Teléfonos

# Mostrar el contenido del carrito
print(f"Carrito de {cliente1}:")
carrito_cliente1.mostrar_contenido()

# Crear una orden y generar la factura
orden_cliente1 = Orden(cliente1, carrito_cliente1)
print("\n" + orden_cliente1.generar_factura())

# Intentar agregar más productos de los que hay disponibles
print("\nIntentando agregar más productos de los disponibles...")
if carrito_cliente1.agregar_producto(producto3, 30):  # 30 Auriculares (pero solo hay 20)
    print("Producto agregado al carrito.")
else:
    print("No hay suficiente cantidad disponible para agregar al carrito.")

# Mostrar el contenido actualizado del carrito
carrito_cliente1.mostrar_contenido()