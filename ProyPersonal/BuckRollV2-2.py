# Sadrach Juan Diego Garcia Flores
# Grupo: 4-2 uth
# Fecha: 23/10/2024

#Inicio de proyecto personal imitando el juego de buckshot roulette, El juego tratara de que el usuario obtendra una escopeta con un 8 tiros
#y cada inicio de ronda dara una cantidad randoms de balas falsas y balas reales(Minimo 1 real), el usuario tendra que elegir entre
#dispararse a si mismo o disparar al oponente, si el usuario se dispara a si mismo podra vivir o morir depende de si es bala falsa o real, 
#si el usuario decide disparar al oponente tendra la posibilidad de matar al oponente dependiendo si es una bala real o falsa,
#si el usuario mata al oponente se le restara una vida al oponente (total de 4 vidas), si el usuario muere se le restara a el 1 vida 
#(total de 4 vidas), el juego terminara cuando uno de los dos llegue a 0 vidas.
#Al inicio de cada ronda el usuario y oponente tendran diferentes "inventario" (Maximo 3 por ronda y si tiene el inventario lleno no podra tener mas
#inventario y se perderan los nuevos inventario, Maximo de 8 inventario) cada uno con una habilidad diferente, tendran la posibilidad de usar cualquier item
#que tenga en su inventario, los inventario seran:
#-Lupa: vera si la bala siguiente es falsa o real
#-Cuchillo: podra cortar el Arma y el DañoArma obtendra x2 de daño en el siguinte tiro (solo 1 vez por ronda)
#-cerveza: Descarta la siguinete bala falsa o real y te dice que bala era
#-cigarro: obtendra 1 vida
#-telefono: le dira la posicion de una de las balas falsas o si no tiene balas falsas le dira "estas muerto"
#-Swaper: podra cambiar las balas falaas por balas reales y las reales por falsas
#-daga: podra robar un item del oponente y se usara instantaneamente
#-cambio: revolvera las balas de la escopeta (balas.Shuffle comando de esta cosa)
#-mas inventario proximamente:
#El usuario podra usar tantos inventario como quira hasata disparar, una vez que dispare no podra usar mas inventario en ese turno y pasara el turno al
#oponente, Al iniciar una nueva ronda se dira cuantas balas son falsas y cuantas reales pero no la posicion en la que este en el DañoArma eso sera
#random.

# cabe recalcar que el juego sera echo en consola al no saber como progranamar en un entorno grafico. 

# En esta version intentare cambiar el codigo para volverlo mas legible y entendible para mi y para los demas, ademas de agregar mas inventario y
# mejorar la jugabilidad del juego.

# Buckshot Roulette Version 2.1
# Inicio de codigo

#Importar librerias
import random
import os
import time
from MisFunciones_2024 import *

Cls()

class Escopeta:
    def __init__(self):
        #ok aqui se crea la clase escopeta con los atributos balas y daño
        self.Balas = []
        self.Daño = 1

    def Cargar(self):
        #aqui se edscoje cuantas balas seran falsas y cuantas reales
        self.balasFalsas = random.randint(1, 7)
        self.balasReales = 8 - self.balasFalsas

    def Contar_balas(self):
        print(f"Balas Falsas: {self.balasFalsas}\nBalas Reales: {self.balasReales}")

    def Insertar(self, Lista, Elemento):
        #Aqui se inserta un elemento en una lista
        if len(Lista) < 8:
            indice = random.randint(0, len(Lista))
            Lista.insert(indice, Elemento)

    def Revolver(self, Lista):
        #Aqui se revuelven las balas y se introducen a la escopeta
        for i in range(self.balasFalsas):
            self.Balas.append("Falsa")
        for i in range(self.balasReales):
            self.Balas.append("Real")
        random.shuffle(self.Balas)

    def Disparar(self, Lista):
        #Bang! Bang! Usuario a si mismo
        if len(Lista) > 0:
            self.Balas.pop(0)
        else:
            return "No hay balas"

    def AumentarDaño(self):
        #Aumentamos el daño
        self.Daño = 2

class Jugador:
    def __init__(self, Nombre):
        #Aqui se crea la clase jugador con los atributos nombre, vida e inventario
        self.Nombre = Nombre
        self.Vida = 4
        self.VidaOP = 4
        self.Inventario = []
        self.InventarioOP = []

    def AgregarItem(self, Item):
        #Aqui se agrega un item al inventario
        if len(self.Inventario) < 8:
            self.Inventario.append(Item)
        else:
            print(f"{self.Nombre} no puede tener más de 8 items.")

    def UsarItem(self, Escopeta):
        #Aqui se usa un item del inventario
        if not self.Inventario:
            print(f"{self.Nombre} no tiene items en el inventario.")
            return
        
        print(f"Inventario de {self.Nombre}:")
        for idx, item in enumerate(self.Inventario, start=1):
            print(f"{idx}. {item}")

        self.opcion = int(input("Elige un item: "))
        itemEncontrado = False

        for idx, item in enumerate(self.Inventario, start=1):
            if idx == self.opcion:
                Item.usar(self, Escopeta)
                self.Inventario.remove(item)
                itemEncontrado = True
                break
            
        if not itemEncontrado:
            print("no tienes el item")

    def UseItemOP(self):
        if len(self.InventarioOP) > 0:
            random.choice(self.InventarioOP)
        else:
            print("pepe no tiene objetos")
            return

    def PerderVida(self, Daño):
        #Aqui se pierde vida
        if self.Vida <= 0:
            print(f"{self.Nombre} ha muerto.")
        else:
            self.Vida -= Daño

class Item:
    def __init__(self,nombre):
        #Aqui se crea la clase item con el atributo nombre
        self.Nombre = nombre

    def usar(self, jugador, escopeta):
        #Aqui se usa el item por el numero seleccionado en class jugador UsarItem
        if self.nombre == "Lupa":
            print(f"La siguiente bala es: {escopeta.balas[0]}")
        elif self.nombre == "Cuchillo":
            if escopeta.daño == 1:
                escopeta.aumentar_daño()
                print("El siguiente tiro hará x2 de daño.")
            else:
                print("Ya no puedes usar el cuchillo.")
        elif self.nombre == "Cerveza":
            if escopeta.balas:
                print(f"La siguiente bala era: {escopeta.balas.pop(0)}")
            else:
                print("No hay balas.")
        elif self.nombre == "Cigarro":
            if jugador.vida < 4:
                jugador.vida += 1
                print(f"{jugador.nombre} ha obtenido una vida.")
            else:
                print("Ya tienes la vida máxima.")
        elif self.nombre == "Telefono":
            if "Falsa" in escopeta.balas:
                print(f"La bala falsa está en la posición {escopeta.balas.index('Falsa') + 1}")
            else:
                print("No hay balas falsas.")
        elif self.nombre == "Swaper":
            escopeta.balas = ["Real" if bala == "Falsa" else "Falsa" for bala in escopeta.balas]
            print("Se han cambiado las balas.")
        elif self.nombre == "Cambio":
            random.shuffle(escopeta.balas)
            print("Se han mezclado las balas.")


class Turno():
    def __init__(self, jugador, oponente, escopeta):
        self.jugador = jugador
        self.oponente = oponente
        self.escopeta = escopeta

    def ronda(self):
        turno_actual = random.choice([self.TurnoUS, self.TurnoOP])
        while self.jugador.Vida > 0 and self.oponente.VidaOP > 0:
            if turno_actual == self.TurnoUS:
                self.TurnoUS()
                turno_actual = self.TurnoOP
            else:
                self.TurnoOP()
                turno_actual = self.TurnoUS

    def TurnoOP(self):
        opcion = [self.escopeta.disparar_OP, self.escopeta.DispararOP_US, self.oponente.UseItemOP]
        elecciones = random.choice(opcion)
        elecciones()

    def TurnoUS(self):
        opcion = int(input("1. Disparar a si mismo\n2. Disparar al oponente\n3. Usar item\nque vas a hacer? "))
        if opcion == 1:
            Escopeta.Disparar(Escopeta.Balas)
        elif opcion == 2:
            Escopeta.Disparar_OP(Escopeta.Balas)
        elif opcion == 3:
            Jugador.UsarItem(Escopeta)
        else:
            print("opcion invalida")

class Juego:
    def __init__(self):
        self.jugador1 = Jugador(input("Nombre del jugador: "))
        self.oponente = Jugador("Pepe")
        self.escopeta = Escopeta()
        self.items_disponibles = {
            Item("Lupa"): 1, Item("Cuchillo"): 2, Item("Cerveza"): 3, Item("Cigarro"): 4, Item("Telefono"): 5,
            Item("Swaper"): 6, Item("Cambio"): 7
        }

    def Iniciar(self):
        while self.jugador1.Vida > 0 and self.oponente.Vida > 0:
            Cls()
            print(f"\nInicio de ronda - Vidas del jugador: {self.jugador1.Vida} - Vidas del oponente: {self.oponente.Vida}")
            self.escopeta.Cargar()
            self.agregar_items(self.jugador1)
            self.agregar_items(self.oponente)
            self.ronda()

        if self.jugador1.Vida <= 0:
            print("Game Over. Has perdido.")
        else:
            print("¡Has ganado!")

        if self.oponente.VidaOP <= 0:
            print("Has ganado.")
        else:
            print("Game Over. Perdiste")

    def agregar_items(self, jugador):
        for _ in range(3):
            item = random.choice(self.items_disponibles)
            jugador.agregar_item(item)

    def ronda(self):
        turno_jugador = True
        while self.jugador.Vida > 0 and self.oponente.VidaOP > 0 and self.escopeta.Balas:
            if turno_jugador:
                self.menu_jugador()
            else:
                self.turno_oponente()
            turno_jugador = not turno_jugador

    def menu_jugador(self):
        Cls()
        print("Balas Restantes: 8")
        print("Balas Falsas: 4\nBalas Reales: 4")
        # print(f"Balas Restantes: {len(self.escopeta.Balas)}")
        # self.escopeta.Contar_balas()
        print("=========================")
        print("1.-Dispararse a si mismo")
        print("2.-Disparar al oponente")
        print("3.-Usar item")
        opcion = int(input("Elije una opcion:"))
        pausa_final()
