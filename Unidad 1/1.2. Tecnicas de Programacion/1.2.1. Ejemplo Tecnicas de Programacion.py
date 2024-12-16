class PersonajeDeFicción:

    def __init__(self, nombre, poder, conocimiento, protección, salud):
        self.nombre = nombre
        self.poder = poder
        self.conocimiento = conocimiento
        self.protección = protección
        self.salud = salud

    def mostrar_atributos(self):
        print(self.nombre, ":", sep="")
        print("·Poder:", self.poder)
        print("·Conocimiento:", self.conocimiento)
        print("·Protección:", self.protección)
        print("·Salud:", self.salud)

    def mejorar_nivel(self, poder, conocimiento, protección):
        self.poder += poder
        self.conocimiento += conocimiento
        self.protección += protección

    def sigue_vivo(self):
        return self.salud > 0

    def derrotado(self):
        self.salud = 0
        print(self.nombre, "ha sido derrotado")

    def calcular_dano(self, rival):
        return self.poder - rival.protección

    def atacar(self, rival):
        dano = self.calcular_dano(rival)
        rival.salud -= dano
        print(self.nombre, "ha causado", dano, "puntos de daño a", rival.nombre)
        if rival.sigue_vivo():
            print("Salud de", rival.nombre, "es", rival.salud)
        else:
            rival.derrotado()


class GuerreroFuerte(PersonajeDeFicción):

    def __init__(self, nombre, poder, conocimiento, protección, salud, arma):
        super().__init__(nombre, poder, conocimiento, protección, salud)
        self.arma = arma

    def cambiar_arma(self):
        seleccion = int(input("Elige un arma: (1) Espada Épica, daño 9. (2) Espada Divina, daño 12"))
        if seleccion == 1:
            self.arma = 9
        elif seleccion == 2:
            self.arma = 12
        else:
            print("Selección de arma errónea")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Arma:", self.arma)

    def calcular_dano(self, rival):
        return self.poder * self.arma - rival.protección


class HechiceroMagico(PersonajeDeFicción):

    def __init__(self, nombre, poder, conocimiento, protección, salud, pergamino):
        super().__init__(nombre, poder, conocimiento, protección, salud)
        self.pergamino = pergamino

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Pergamino:", self.pergamino)

    def calcular_dano(self, rival):
        return self.conocimiento * self.pergamino - rival.protección


def enfrentamiento_final(personaje_1, personaje_2):
    turno = 0
    while personaje_1.sigue_vivo() and personaje_2.sigue_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", personaje_1.nombre, ":", sep="")
        personaje_1.atacar(personaje_2)
        print(">>> Acción de ", personaje_2.nombre, ":", sep="")
        personaje_2.atacar(personaje_1)
        turno += 1
    if personaje_1.sigue_vivo():
        print("\nGanador:", personaje_1.nombre)
    elif personaje_2.sigue_vivo():
        print("\nGanador:", personaje_2.nombre)
    else:
        print("\nEs un empate")


personaje_1 = GuerreroFuerte("Thor", 25, 8, 5, 150, 7)
personaje_2 = HechiceroMagico("Merlin", 10, 20, 4, 120, 5)

personaje_1.mostrar_atributos()
personaje_2.mostrar_atributos()

enfrentamiento_final(personaje_1, personaje_2)
