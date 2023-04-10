flag = 0

while flag == 0:
    numero0 = input(str("Ingrese número para la ACL, o envíe un 0 para salir: "))
    numero = int(numero0)
    if 1 <= numero <= 99:
        print("El número ingresado corresponde a una ACL Estándar")
    elif 100 <= numero <= 199:
        print("El número ingresado corresponde a una ACL Extendida")

    elif 1300 <= numero <= 1999:
        print("El número ingresado corresponde a una ACL Estándar (Rango Extendido)")

    elif 2000 <= numero <= 2699:
        print("El número ingresado corresponde a una ACL Extendida (Rango Extendido)")
    elif numero == 0:
        flag = 1
    else:
        print("El número ingresado no es válido para una ACL")
