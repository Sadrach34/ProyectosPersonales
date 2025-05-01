from MisFunciones_2024 import *
import random
import time

Cls()
D4 = [1, 2, 3, 4]
D6 = [1, 2, 3, 4, 5, 6]
D8 = [1, 2, 3, 4, 5, 6, 7, 8]
D10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
D20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
DPorcentual = [10,20,30,40,50,60,70,80,90,100]

razas = ["Humano" , "Elfo", "Enano", "Mediano", "Semielfo", "Semiorco"]
clases = ["Guerrero", "Mago", "Pícaro", "Clérigo", "Bardo", "Explorador"]

# Stats de raza
stats_razas = {
    "Humano": {
        "Fuerza": 1,
        "Destreza": 1,
        "Constitución": 1,
        "Inteligencia": 1,
        "Sabiduría": 1,
        "Carisma": 1
    },
    "Elfo": {
        "Fuerza": 0,
        "Destreza": 2,
        "Constitución": 0,
        "Inteligencia": 1,
        "Sabiduría": 0,
        "Carisma": 0
    },
    "Enano": {
        "Fuerza": 0,
        "Destreza": 0,
        "Constitución": 2,
        "Inteligencia": 0,
        "Sabiduría": 1,
        "Carisma": 0
    },
    "Mediano": {
        "Fuerza": 0,
        "Destreza": 2,
        "Constitución": 0,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 1
    },
    "Semielfo": {
        "Fuerza": 0,
        "Destreza": 2,
        "Constitución": 0,
        "Inteligencia": 1,
        "Sabiduría": 0,
        "Carisma": 0
    },
    "Semiorco": {
        "Fuerza": 2,
        "Destreza": 0,
        "Constitución": 1,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 0
    }
}

# Stats de clase
stats_clases = {
    "Guerrero": {
        "Fuerza": 2,
        "Destreza": 0,
        "Constitución": 1,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 0
    },
    "Mago": {
        "Fuerza": 0,
        "Destreza": 0,
        "Constitución": 0,
        "Inteligencia": 2,
        "Sabiduría": 0,
        "Sabiduría": 1
    },
    "Pícaro": {
        "Fuerza": 0,
        "Destreza": 2,
        "Constitución": 0,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 1
    },
    "Clérigo": {
        "Fuerza": 0,
        "Destreza": 0,
        "Constitución": 0,
        "Inteligencia": 1,
        "Sabiduría": 2,
        "Carisma": 0
    },
    "Bardo": {
        "Fuerza": 0,
        "Destreza": 1,
        "Constitución": 0,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 2,
    },
    "Explorador": {
        "Fuerza": 0,
        "Destreza": 2,
        "Constitución": 0,
        "Inteligencia": 0,
        "Sabiduría": 1,
        "Carisma": 0
    }
}

def Stats():
    # Definición de las estadísticas
    stats = {
        "Fuerza": 0,
        "Destreza": 0,
        "Constitución": 0,
        "Inteligencia": 0,
        "Sabiduría": 0,
        "Carisma": 0
    }

    # Generación de estadísticas aleatorias
    for stat in stats.keys():
        # Lanzar 4d6 y sumar los 3 mayores
        rolls = random.sample(D6, 4)
        rolls.remove(min(rolls))
        stats[stat] = sum(rolls)

    return stats

estadisticas = Stats()
while True:
    print("Bienvenido a la hoja de personaje de D&D 5e")
    print("Vamos a generar tus estadísticas de personaje")
    print("")
    print("Selecciona tu raza:")
    for i, raza in enumerate(razas):
        print(f"{i + 1}. {raza}")
    seleccion_razas = int(input("Selecciona una opción: ")) - 1
    if 0 <= seleccion_razas < len(razas):
        raza_seleccionada = razas[seleccion_razas]
        print(f"Has seleccionado la raza: {raza_seleccionada}")

        print("")
        print("Selecciona tu clase:")
        for i, clase in enumerate(clases):
            print(f"{i + 1}. {clase}")
        seleccion_clases = int(input("Selecciona una opción: ")) - 1
        if 0 <= seleccion_clases < len(clases):
            clase_seleccionada = clases[seleccion_clases]
            print(f"Has seleccionado la clase: {clase_seleccionada}")

            print("")
            print("Tus estadísticas con raza y clase son:")
            print("Fuerza: ", estadisticas["Fuerza"] + stats_clases[clase_seleccionada]["Fuerza"])
            print("Destreza: ", estadisticas["Destreza"] + stats_clases[clase_seleccionada]["Destreza"])
            print("Constitución: ", estadisticas["Constitución"] + stats_clases[clase_seleccionada]["Constitución"])
            print("Inteligencia: ", estadisticas["Inteligencia"] + stats_clases[clase_seleccionada]["Inteligencia"])
            print("Sabiduría: ", estadisticas["Sabiduría"] + stats_clases[clase_seleccionada]["Sabiduría"])
            print("Carisma: ", estadisticas["Carisma"] + stats_clases[clase_seleccionada]["Carisma"])
        else:
            print("Selección inválida. Intenta de nuevo.")
            continue
        break
    else:
        print("Selección inválida. Intenta de nuevo.")


