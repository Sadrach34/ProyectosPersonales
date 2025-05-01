Dia = int(input("Dame un número de la seana: "))

print("Con if")
if Dia == 1:
    print("Lunes")
elif Dia == 2:
    print("Martes")
elif Dia == 3:
    print("Miércoles")
elif Dia == 4:
    print("Jueves")
elif Dia == 5:
    print("Viernes")
elif Dia == 6:
    print("Sábado")
elif Dia == 7:
    print("Domingo")
else:
    print("Número de día incorrecto")

print("\nCon case")
match Dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número de día incorrecto")

print("\nCon lista")
Semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
Semana = [1,2,3,4,5,6,7,8,9]
print(Semana[Dia - 1])
