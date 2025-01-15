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

# Buckshot Roulette Version 2.0
# Inicio de codigo
import random
import os
import time
from MisFunciones_2024 import *

# Definición de la lista de balas y otras variables globales
vidas = 4
vidasOP = 4
items = {1:"Lupa", 2:"cuchillo", 3:"cerveza", 4:"cigarro", 5:"telefono", 6:"Swaper", 7:"daga", 8:"cambio"}
inventario = []
inventariOP = []
DañoArma = 1

#Para probar si se reinicia la variable de daño
def daño():
    global DañoArma
    DañoArma = 1
    return DañoArma

# La suma de las balas falsas y reales no puede ser mayor a 8
balas_falsas = random.randint(1, 7)
balas_reales = 8 - balas_falsas

Balas = []

def insertar_balas(Lista, Elemento):
    if len(Lista) < 8:
        indice = random.randint(0, len(Lista))
        Lista.insert(indice, Elemento)

# Insertar balas falsas y reales a la lista de balas
for i in range(balas_falsas):
    insertar_balas(Balas, "Falsa")
for i in range(balas_reales):
    insertar_balas(Balas, "Real")

random.shuffle(Balas)

# Menu de inicio
def menu():
    print("Bienvenido a Buckshot Roulette v1.6")
    print("1) Jugar")
    print("2) Reglas")
    print("3) Salir")

# Menu de juego
def ShotRoullete():
    print(f"Tienes una escopeta con {len(Balas)} tiros")
    print("1) Disparar a ti mismo")
    print("2) Disparar al oponente")
    print("3) Ver inventario")

#El usuario y oponente obtendra un item random
def obtenerItem():
    Cls()
    print("La caja se abre, dento hay: ")
    for i in range(3):
        item = random.choice(items)
        inventario.append(item)
    print(inventario)

    for i in range(3):
        item = random.choice(items)
        inventariOP.append(item)
    print(inventariOP)

#El usuario podra elegir un item de su inventario
def UseItem():
    global inventario
    Cls()
    print("Inventario: ", inventario)
    item = input("Que item quieres usar: ")
    if item in inventario:
        if item == "Lupa":
            lupa()
        elif item == "cuchillo":
            cuchillo()
        elif item == "cerveza":
            cerveza()
        elif item == "cigarro":
            cigarro()
        elif item == "telefono":
            telefono()
        elif item == "Swaper":
            Swaper()
        elif item == "daga":
            daga()
        elif item == "cambio":
            cambio()
        else:
            print("Item no valido")
    else:
        print("Item no disponible")

def UseItemOP():
    global inventario
    Cls()
    item = random.choice(inventariOP)
    if item in inventario:
        if item == "Lupa":
            lupa()
        elif item == "cuchillo":
            cuchillo()
        elif item == "cerveza":
            cerveza()
        elif item == "cigarro":
            cigarro()
        elif item == "telefono":
            telefono()
        elif item == "Swaper":
            Swaper()
        elif item == "daga":
            daga()
        elif item == "cambio":
            cambio()
        else:
            print("Item no valido")
    else:
        print("Item no disponible")

#Item de lupa: vera si la bala siguiente es falsa o real
def lupa():
    print(f"La siguinete bala es {Balas[0]}")
    pausa()

#Item de cuchillo: podra cortar el Arma
def cuchillo():
    global DañoArma
    if DañoArma == 2:
        print("Cuchillo: La escopeta ya se corto")
        return
    else:
        print("La escopeta ahora matara mejor")
        DañoArma *= 2
        return DañoArma

#Item de cigarro: obtendra 1 vida
def cigarro():
    global vidas
    print("Cigarro: fumando vida")
    if vidas < 4:
        vidas += 1
    else:
        print("sientes como la vida se te va enves de volver")
    return vidas

#Item de telefono: le dira la posicion de una de las balas falsas o si no tiene balas falsas le dira "estas muerto"
def telefono():
    print(Balas)
    print("Telefono: ")
    print("*Ring Ring*")
    if "Falsa" in Balas:
        print("Hay una bala falsa en la posicion:", Balas.index("Falsa")+1)
    else:
        print("Estas muerto")

#Item de swaper: podra cambiar las balas falaas por balas reales y las reales por falsas
def Swaper():
    print("Swaper: ")
    for i in range(8):
        if Balas[i] == "Falsa":
            Balas[i] = "Real"
        else:
            Balas[i] = "Falsa"
    print("Balas cambiadas")

#Item de daga: podra robar un item del oponente y se usara instantaneamente
def daga():
    print("Daga: ")
    #mas tarde

#Item de cerveza: Elimina la siguiente bala
def cerveza():
    if Balas[0] == "Falsa":
        print("Cerveza: la siguiente bala era falsa y fue descartada")
        Balas.pop(0)
    else:
        print("Cerveza: la siguiente bala era real y fue descartada")
        Balas.pop(0)

def cambio():
    pass

# Turno del oponente
def turnoOP():
    opciones = [dispararTurnOP, dispararUSTurnOP, UseItemOP]
    elecciones = random.choice(opciones)
    elecciones()
def dispararTurnOP():
    global vidasOP
    Cls()
    print("Disparando...")
    time.sleep(1)
    if Balas[0] == "Falsa":
        print(f"Pepe todavía tiene {vidasOP} vidas")
        if len(Balas) <= 0:            
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
        pausa()
    else:
        vidasOP -= DañoArma
        print("Pepe murió")
        if vidasOP <= 0:
            print("Game Over\nPepe se mató solo jijijija")
            pausa()
            return False
        else:
            print(f"A Pepe le quedan {vidasOP} vidas, Reviviendo...")
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
            pausa()
    Balas.pop(0)
    return True
def dispararUSTurnOP():
    global Balas
    global vidas
    Cls()
    print("Disparando...")
    time.sleep(1)
    if Balas[0] == "Falsa":
        print("Pepe se pone triste porque no te mató. Te quedan", vidas, "vidas, sobrevives un minuto más")
        if len(Balas) <= 0:            
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
        pausa()
    else:
        vidas -= DañoArma
        print("La bala era real, Pepe está feliz porque te mató. Te quedan:", vidas, "vidas")
        if vidas <= 0:
            print("Pepe celebra que te mató")
            pausa()
            return False
        else:
            print("Pepe celebra que te mató. Te quedan:", vidas, "vidas, Reviviendo...")
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
            pausa()
    Balas.pop(0)
    return True

# Turno del usuario
def disparar():
    global Balas
    global vidas
    Cls()
    print("Disparando...")
    time.sleep(1)
    if Balas[0] == "Falsa":
        print("La bala era falsa. Te quedan", vidas, "vidas, sobrevives un minuto más")
        if len(Balas) <= 0:            
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
        pausa()
    else:
        vidas -= DañoArma
        print("La bala era real. Estás muerto. Te quedan:", vidas, "vidas")
        if vidas == 0:
            print("Game Over\nPepe se ríe porque te mataste solo")
            pausa()
            return False
        else:
            print("Te quedan", vidas, "vidas, Reviviendo...")
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
            pausa()
    Balas.pop(0)
    return True
def dispararOP():
    global Balas
    global vidasOP
    Cls()
    print("Disparando...")
    time.sleep(1)
    if Balas[0] == "Falsa":
        print("Suerte a la próxima. A Pepe le quedan:", vidasOP, "vidas, sobrevives un minuto más")
        if len(Balas) <= 0:            
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
        pausa()
    else:
        vidasOP -= DañoArma
        print("La bala era real. Mataste a Pepe. Le quedan:", vidasOP, "vidas")
        if vidasOP <= 0:
            print("Ganaste\nMataste a Pepe. Felicidades, ganaste\nPepe era un criminal mutilador de gatos\nFelicidades, Shinji")
            pausa()
            return False
        else:
            print("Felicidades, mataste a Pepe. Le quedan:", vidasOP, "vidas, Reviviendo...")
            Balas.clear()
            for i in range(balas_falsas):
                insertar_balas(Balas, "Falsa")
            for i in range(balas_reales):
                insertar_balas(Balas, "Real")
            pausa()
    Balas.pop(0)
    return True

# Inicio de juego
Cls()
menu()
opcion = input("Elige una opción: ")
while opcion != "3":
    if opcion == "1":
        while True:
            if vidasOP <= 0 or vidas <= 0:
                break
            obtenerItem()
            print(f"Balas falsas: {balas_falsas}\nBalas reales: {balas_reales}")
            ShotRoullete()
            opcion = input("Elige una opción: ")
            if opcion == "1":
                if not disparar():
                    break
            elif opcion == "2":
                if not dispararOP():
                    break
            elif opcion == "3":
                UseItem()
            else:
                print("Opción inválida")
            turnoOP()
            if vidasOP <= 0 or vidas <= 0:
                break
    elif opcion == "2":
        Cls()
        print("Reglas del juego")
        print("El juego consiste en una escopeta con 8 tiros. Cada ronda se dará una cantidad random de balas falsas y reales.")
        print("El jugador tendrá que elegir entre dispararse a sí mismo o disparar a su contrincante. Una vez que dispare, no podrá usar más inventario.")
        print("El juego terminará cuando uno de los dos llegue a 0 vidas.")
        print("El juego es completamente random y no se puede saber si la bala es falsa o real.")
        print("Presiona Enter para continuar y jugar >:D")
        pausa()
    else:
        print("Opción inválida")
    Cls()
    menu()
    opcion = input("Elige una opción: ")