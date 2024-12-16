# Programación Tradicional
# Ejemplo: Administración de una cuenta bancaria

# Definición de variables globales
balance = 0
tasa_de_interes = 0.05

# Función para realizar un depósito en la cuenta
def depositar(cantidad):
    global balance
    balance += cantidad

# Función para realizar un retiro de la cuenta
def retirar_fondos(cantidad):
    global balance
    balance -= cantidad

# Función para calcular los intereses y actualizar el saldo
def aplicar_intereses():
    global balance, tasa_de_interes
    intereses = balance * tasa_de_interes
    balance += intereses

# Uso de las funciones en la programación tradicional
depositar(1000)
retirar_fondos(500)
aplicar_intereses()

# Imprimir el balance final
print("Balance (Tradicional):", balance)


# Programación Orientada a Objetos (POO)
# Ejemplo: Administración de una cuenta bancaria

class CuentaBancaria:
    def __init__(self, balance_inicial=0, tasa_de_interes=0.05):
        self.balance = balance_inicial
        self.tasa_de_interes = tasa_de_interes

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar_fondos(self, cantidad):
        self.balance -= cantidad

    def aplicar_intereses(self):
        intereses = self.balance * self.tasa_de_interes
        self.balance += intereses

# Crear una instancia de la clase CuentaBancaria
cuenta_usuario = CuentaBancaria()

# Uso de los métodos en la programación orientada a objetos
cuenta_usuario.depositar(1000)
cuenta_usuario.retirar_fondos(500)
cuenta_usuario.aplicar_intereses()

# Imprimir el balance final
print("Balance (POO):", cuenta_usuario.balance)
