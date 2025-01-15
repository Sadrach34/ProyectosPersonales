# Sadrach Juan Diego Garcia Flores
# Grupo: 4-2 uth
# Fecha: 23/10/2024

#mejorare el codigo de buckshot roulette y el juego en si para que sea mas parecido a la version real

# Buckshot Roulette Version 3.0
# Inicio de codigo

import random
import os
import time
import pygame
from MisFunciones_2024 import *
from playsound import playsound

Cls()

class Escopeta():
    def __init__(self):
        self.balas = []
        self.Daño = 1

    def cargar(self):
        self.balas_falsas = random.randint(1, 7)
        self.balas_reales = 8 - self.balas_falsas
        for i in range(self.balas_falsas):
            self.balas.append('Falsa')
            # playsound('c:/Users/Sadrach/Desktop/ProyPersonal/sonidos/Recarga.mp3')
        for i in range(self.balas_reales):
            self.balas.append('Real')
            # playsound('c:/Users/Sadrach/Desktop/ProyPersonal/sonidos/Recarga.mp3')
        random.shuffle(self.balas)

    def contar_balas(self):
        print(f'Balas falsas: {self.balas_falsas}\nBalas reales: {self.balas_reales}')
        print(f"Las balas restantes son: {len(self.balas)}")

    def disparar(self):
        self.balas = self.balas.pop()
        # playsound('C:/Users/Sadrach/Desktop/ProyPersonal/sonidos/Disparo.mp3')

    def AumentoDaño(self):
        self.Daño = 2

class Ronda():
    def __init__(self):
        self.ronda = 1

    def contar_ronda(self):
        if self.ronda > 3:
            print("El juego ha terminado")
            return
        else:
            self.ronda += 1
            print(f"Ronda {self.ronda}")

class Jugador():
    def __init__(self, nombre):
        self.Jugador1 = nombre
        self.Jugador2 = 'pepe'
        self.vida_jugador = 4
        self.vida_oponente = 4
        self.items = Items()
        self.inve_jugador = []
        self.inve_oponente = []

    def Caja(self):#Caja entregara los items a los jugadores
        if Ronda.ronda == 1:
            for i in range(2):
                #inve_jugador del jugador
                if len(self.inve_jugador) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_jugador.append(item)
                #inve_jugador del oponente
                if len(self.inve_oponente) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_oponente.append(item)
        elif Ronda.ronda == 2:
            for i in range(3):
                #inve_jugador del jugador
                if len(self.inve_jugador) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_jugador.append(item)
                #inve_jugador del oponente
                if len(self.inve_oponente) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_oponente.append(item)
        elif Ronda.ronda >= 3:
            for i in range(4):
                #inve_jugador del jugador
                if len(self.inve_jugador) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_jugador.append(item)
                #inve_jugador del oponente
                if len(self.inve_oponente) >= 8:
                    print("inve_jugador lleno")
                else:
                    item = random.choice(list(self.items.items.keys()))
                    self.inve_oponente.append(item)

    def UsarItems(self):
        print("Items")
        print("==============================")
        for i in range(len(self.inve_jugador)):
            print(f"{i + 1}. {self.inve_jugador[i]}")
        print("==============================")
        opcion = input("Seleccione un item: ")
        #Me lo dio Copilot
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.inve_jugador):
            item_seleccionado = self.inve_jugador[int(opcion) - 1]
            if item_seleccionado == 'Lupa':
                self.items.Lupa()
            elif item_seleccionado == 'Cuchillo':
                self.items.Cuchillo()
            elif item_seleccionado == 'Cerveza':
                self.items.Cerveza()
            elif item_seleccionado == 'Cigarro':
                self.items.Cigarro()
            elif item_seleccionado == 'Telefono':
                self.items.Telefono()
            elif item_seleccionado == 'Swaper':
                self.items.Swaper()
            elif item_seleccionado == 'Adrenalina':
                self.items.Adrenalina()
            else:
                print("Item no reconocido")
        else:
            print("Opcion invalida o item no disponible")

    def perderVida(self):
        self.vida_jugador -= Escopeta
class Turno():
    def __init__(self):
        self.turno = True

    def cambiar_turno(self):
        if self.turno == True:
            print("Es el turno del jugador 1")
            Juego.MenuJuego()
            self.turno = not self.turno
        else:
            print("Es el turno del jugador 2")
            self.turno = True

    #Aqui definire el turno del jugador y el oponente
    def Turno(self):
        if self.opcion == '1':
            Escopeta.disparar()

            

class Items():
    def __init__(self):
        self.items = {'Lupa': 1, 'Cuchillo': 2, 'Cerveza': 3, 'Cigarro': 4, 'Telefono': 5, 'Swaper': 6, 'Adrenalina': 7}

    def Lupa(self):
        print(f"La siguiente bala es: {Escopeta.balas[0]}")

    def Cuchillo(self):
        print("La escopeta mata mejor")
        Escopeta.AumentoDaño()

    def cerbeza(self):
        Escopeta.balas.pop(0)

    def cigarro(self):
        Jugador.vida_jugador += 1

    def telefono(self):
        telefono1 = random.randint(0,len(Escopeta.balas))
        telefono2 = Escopeta.balas[telefono1]
        print(f"La bala {telefono1} es {telefono2}")

    def swaper(self):
        Escopeta.balas = ["Real" if balas == "Falsa" else "Falsa" for balas in Escopeta.balas]
        print("Inverso")

    def Adrenalina(self):
        # Roba un item del oponente a eleccion y se utiliza en el mismo turno
        print("Robando item")
        print("Items")
        print("==============================")
        for i in range(len(Jugador.inve_oponente)):
            print(f"{i + 1}. {Jugador.inve_oponente[i]}")
        print("==============================")
        opcion = input("Seleccione un item: ")

        if opcion.isdigit() and 1 <= int(opcion) <= len(Jugador.inve_oponente):
            item_robado = Jugador.inve_oponente.pop(int(opcion) - 1)
            Jugador.inve_jugador.append(item_robado)
            
            # Usar el ítem robado inmediatamente
            if item_robado == 'Lupa':
                self.Lupa()
            elif item_robado == 'Cuchillo':
                self.Cuchillo()
            elif item_robado == 'Cerveza':
                self.Cerveza()
            elif item_robado == 'Cigarro':
                self.Cigarro()
            elif item_robado == 'Telefono':
                self.Telefono()
            elif item_robado == 'Swaper':
                self.Swaper()
            elif item_robado == 'Adrenalina':
                self.Adrenalina()
            else:
                print("Item no reconocido")
        else:
            print("Opcion invalida")

class Juego():
    def __init__(self):
        self.juego = True

    def Menu(self):
        print("1. Jugar")
        print("2. About")
        print("3. Opciones")
        print("4. salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            self.MenuJuego()
        elif opcion == '2':
            print("Buckshot Roulette Version 3.0")
            print("Juego Desarrollado por Sadrach Juan Diego Garcia Flores")
            print("basado en el juego de BuckShot Roulette")
            print("Este juego no se hace responsable de el uso de las personas")
            print("Solo es un juego para probar mis capacidades de programacion")   
            print("Se proibe la venta del juego, Si compraste el juego de alguien mas, te estafaron Sorry")   
            print("Si quieres jugarlo, Compra el juego original en steam, muy recomendable")    
            print("lo mejor que puedes hacer es apoyar a los desarrolladores originales")   
            print("Gracias <3")   
        elif opcion == '3':
            print("wey no hay opciones")
            print("Solo es un juego de prueba y esto es de broma xd")
            pausa()
            return
        elif opcion == '4':
            print("Gracias por jugar")
            self.juego = False
        else:
            print("Opcion invalida")
    
    def MenuJuego(self):
        while self.vida_jugador > 0 and self.vida_oponente > 0:
            Jugador.Caja()
            print(f"Tienes: {Jugador.inve_jugador}")
            pausa()
            Cls()
            print("Menu")
            print("==============================")
            print("1. Dispararse a si mismo")
            print("2. Dispararse al oponente")
            print("3. Usar items")
            self.opcion = input("Seleccione una opcion: ")
            if self.opcion == '1':
                print("Disparandose a si mismo")
                Escopeta.disparar()
                Jugador.vida_jugador -= Escopeta.Daño

            elif self.opcion == '2':
                print("Disparandole al oponente")
                Escopeta.disparar()
                Jugador.vida_oponente -= Escopeta.Daño

            elif self.opcion == '3':
                print("Usando items")
                Jugador.UsarItems()
            else:
                print("Opcion invalida")
        else:
            pass

Juegos = Juego()
Juegos.Menu