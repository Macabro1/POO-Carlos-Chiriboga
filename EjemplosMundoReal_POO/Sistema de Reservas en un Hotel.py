# Definimos la clase "Habitacion" que representará las habitaciones del hotel.
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (individual, doble, etc.)
        self.precio = precio  # Precio por noche
        self.reservada = False  # Estado de la habitación (si está reservada o no)

    def reservar(self):
        """Reserva la habitación si no está ya reservada."""
        if not self.reservada:
            self.reservada = True
            return True
        else:
            return False

    def liberar(self):
        """Libera la habitación (la hace disponible)."""
        self.reservada = False

    def __str__(self):
        """Representación de la habitación como una cadena de texto."""
        estado = "reservada" if self.reservada else "disponible"
        return f"Habitación {self.numero} ({self.tipo}) - {estado}, Precio: ${self.precio}"

# Definimos la clase "Cliente" que representará a los clientes que hacen reservas.
class Cliente:
    def __init__(self, nombre, documento_identidad):
        self.nombre = nombre  # Nombre del cliente
        self.documento_identidad = documento_identidad  # Documento de identidad del cliente

    def __str__(self):
        """Representación del cliente como una cadena de texto."""
        return f"Cliente: {self.nombre} (ID: {self.documento_identidad})"

# Definimos la clase "Reserva" que maneja las reservas de los clientes.
class Reserva:
    def __init__(self, cliente, habitacion, numero_noches):
        self.cliente = cliente  # Cliente que realiza la reserva
        self.habitacion = habitacion  # Habitación reservada
        self.numero_noches = numero_noches  # Número de noches de la reserva
        self.total = self.calcular_total()  # Total de la reserva

    def calcular_total(self):
        """Calcula el costo total de la reserva."""
        return self.habitacion.precio * self.numero_noches

    def __str__(self):
        """Representación de la reserva como una cadena de texto."""
        return f"Reserva de {self.cliente} para {self.habitacion}. Total: ${self.total}"

# Crear instancias de habitaciones
habitacion1 = Habitacion(101, "Individual", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Crear un cliente
cliente1 = Cliente("Carlos Chiriboga", "1711198828")

# Hacer una reserva
if habitacion1.reservar():
    reserva1 = Reserva(cliente1, habitacion1, 3)  # Reserva de 3 noches
    print(reserva1)  # Imprimir los detalles de la reserva
else:
    print("La habitación no está disponible.")

# Intentar reservar una habitación ya reservada
if habitacion1.reservar():
    reserva2 = Reserva(cliente1, habitacion1, 2)
    print(reserva2)
else:
    print("La habitación 101 ya está reservada.")

# Liberar una habitación
habitacion1.liberar()
print(f"Después de liberar: {habitacion1}")

# Volver a intentar hacer la reserva
if habitacion1.reservar():
    reserva3 = Reserva(cliente1, habitacion1, 2)  # Reserva de 2 noches
    print(reserva3)
else:
    print("La habitación no está disponible.")