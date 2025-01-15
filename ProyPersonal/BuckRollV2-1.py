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
        self.balas = []
        self.daño = 1

    def cargar_balas(self):
        self.balas_falsas = random.randint(1, 7)
        self.balas_reales = 8 - self.balas_falsas
        self.balas = ["Falsa"] * self.balas_falsas + ["Real"] * self.balas_reales
        random.shuffle(self.balas)

    def contar_balas(self):
        print(f"Balas falsas: {self.balas_falsas} - Balas reales: {self.balas_reales}")

    def aumentar_daño(self):
        # Duplica el daño
        self.daño = 2

    def disparar(self):
        # Remueve la primera bala y la devuelve
        if self.balas:
            return self.balas.pop(0)
        return None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 4
        self.inventario = []

    def agregar_item(self, item):
        # Agrega item al inventario si hay espacio
        if len(self.inventario) < 8:
            self.inventario.append(item)
        else:
            print(f"{self.nombre} no puede tener más de 8 items.")

    def usar_item(self, escopeta):
        # Usa un item del inventario
        if not self.inventario:
            print(f"{self.nombre} no tiene items en el inventario.")
            return

        print(f"Inventario de {self.nombre}: {[item.nombre for item in self.inventario]}")
        item_nombre = input("¿Qué item desea usar? ")
        for item in self.inventario:
            if item.nombre == item_nombre:
                item.usar(self, escopeta)
                self.inventario.remove(item)
                break
        else:
            print(f"{self.nombre} no tiene el item {item_nombre}")

    def perder_vida(self, daño):
        # Resta vida en función del daño
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} ha muerto.")
            return False
        return True

class Item:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self, jugador, escopeta):
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

class Juego:
    def __init__(self):
        self.jugador1 = Jugador("Jugador1")
        self.oponente = Jugador("Pepe")
        self.escopeta = Escopeta()
        self.items_disponibles = [
            Item("Lupa"), Item("Cuchillo"), Item("Cerveza"), Item("Cigarro"), Item("Telefono"),
            Item("Swaper"), Item("Cambio")
        ]

    def iniciar_juego(self):
        while self.jugador1.vida > 0 and self.oponente.vida > 0:
            Cls()
            print(f"\nInicio de ronda - Vidas del jugador: {self.jugador1.vida} - Vidas del oponente: {self.oponente.vida}")
            self.escopeta.cargar_balas()
            self.entregar_items(self.jugador1)
            self.entregar_items(self.oponente)
            self.ronda()

        if self.jugador1.vida <= 0:
            print("Game Over. Has perdido.")
        else:
            print("¡Has ganado!")

    def entregar_items(self, jugador):
        for _ in range(3):
            item = random.choice(self.items_disponibles)
            jugador.agregar_item(item)

    def ronda(self):
        turno_jugador = True
        while self.jugador1.vida > 0 and self.oponente.vida > 0 and self.escopeta.balas:
            if turno_jugador:
                self.menu_jugador()
            else:
                self.turno_oponente()
            turno_jugador = not turno_jugador

    def menu_jugador(self):
        Cls()
        print("\nTurno del jugador")
        print(f"Balas restantes: {len(self.escopeta.balas)}")
        self.escopeta.contar_balas()
        print("1. Disparar a ti mismo")
        print("2. Disparar al oponente")
        print("3. Usar item")
        opcion = input("¿Qué desea hacer? ")
        print("...")
        time.sleep(2)
        Cls()

        if opcion == "1":
            self.disparar(self.jugador1)
        elif opcion == "2":
            self.disparar(self.oponente)
        elif opcion == "3":
            self.jugador1.usar_item(self.escopeta)

    def disparar(self, objetivo):
        resultado = self.escopeta.disparar()
        if resultado == "Real":
            if not objetivo.perder_vida(self.escopeta.daño):
                print(f"{objetivo.nombre} ha muerto.")
                return
        else:
            print(f"{objetivo.nombre}: La bala era falsa")

    def turno_oponente(self):
        time.sleep(2)
        print("\nTurno del oponente")
        if self.oponente.inventario:
            item = random.choice(self.oponente.inventario)
            item.usar(self.oponente, self.escopeta)
            self.oponente.inventario.remove(item)
            print(f"{self.oponente.nombre} ha usado {item.nombre}")
        else:
            if random.choice([True, False]):
                self.disparar(self.jugador1)
            else:
                print(f"{self.oponente.nombre} no tiene items para usar.")

# Iniciar el juego
juego = Juego()
juego.iniciar_juego()
