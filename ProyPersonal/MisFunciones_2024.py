'''
Archivo: Mis_Funciones_2024.py

Autor: Prof. José Padilla Duarte
Email: jopadu@gmail.com
Fecha de última modificación: 27-septiembre-2024

Descripción: Este código provee de funciones de utilería de uso frecuente que pueden ser 
    utilizadas por nuestras prácticas sin necesidad de reescribir a las mismas.
'''
from msvcrt import getch
import os
import winsound

# ------------- Funciones -------------
def beep_error():
    ''' Produce un sonido especial con el que identificamos una situación irregular. '''
    winsound.Beep(880,125)
    winsound.Beep(700,125)


def leer_int(msj: str):
    ''' Leer un valor entero validado. '''
    while True:
        try:
            return int(input(msj))
        except:
            beep_error()
            print("Error! Debe dar un número entero. Intente de nuevo.\n")


def leer_float(msj: str):
    ''' Leer un valor de punto flotante (decimal) validado. '''
    while True:
        try:
            return float(input(msj))
        except:
            beep_error()
            print("Error! Debe dar un número entero. Intente de nuevo.\n")


def leer_tecla(msj=""):
    ''' Leer una tecla sin necesidad de pulsar Enter. '''
    print(msj, end="", flush=True)     # El flush=True es para que imprima la línea de una vez.
    tecla = getch()
    # print(ord(tecla))     # Para saber el código de la tecla pulsada
    if tecla == b'\x1b':    # ESC
        return "Escape"
    else:
        return tecla.decode("ANSI")


def Cls():
    ''' Limpiar la consola. '''
    if os.name == 'nt':
        os.system("CLS")        # Windows
    else:
        os.system("Clear")      # Linux, iOS o MacOS


def pausa_final():
    print("Presione una tecla para Terminar.")
    getch()


def pausa(msj=""):
    ''' Permite hacer una pausa hasta que el usuario presione una tecla. 
    También puede mostrar un mensaje personalizado si éste se indica en el parámetro msj. '''
    print(msj, end="", flush=True)
    return getch()