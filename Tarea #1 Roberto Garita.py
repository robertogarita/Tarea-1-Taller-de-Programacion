#FUNCION PRINCIPAL #1
#de base 10 a cualquier otra base

def funcion1(numero,base):
    cadena='0123456789' #aqui se ponen todos los digitos de la base mas alta en este caso base 9
    if numero<base:
        return cadena[numero]
    else:
        return funcion1(numero//base,base)+cadena[numero%base]

#pruebas de la funcion
def funcion1_pruebas():
    try:
        assert funcion1(37,3)=="1101"
        assert funcion1(38,3)=="1102"
        print("Las pruebas de la funcion 1 estan: CORRECTO")
    except:
        print("Las pruebas de la funcion 1 estan: INCORRECTO")

funcion1_pruebas()

#--------------------------------------------------------------------------------

#FUNCION PRINCIPAL #2
#de cualquier base a base 10

#funcion auxiliar
def largo(n):
    if n<10:
        return 1
    else:
        return 1 + largo(n//10)

#pruebas de la funcion de largo
def largo_pruebas():
    try:
        assert largo(12345)==5
        assert largo(10987654321)==11
        print("Las pruebas de la funcion largo estan: CORRECTO")
    except:
        print("Las pruebas de la funcion largo estan: INCORRECTO")

largo_pruebas()

def funcion2(numero,base):
    if numero<10:
        return numero
    else:
        return (numero//10**(largo(numero)-1))*base**(largo(numero)-1)+funcion2(numero%10**(largo(numero)-1),base)

#pruebas de la funcion
def funcion2_pruebas():
    try:
        assert funcion2(315,7)==159
        assert funcion2(316,7)==160
        print("Las pruebas de la funcion 2 estan: CORRECTO")
    except:
        print("Las pruebas de la funcion 2 estan: INCORRECTO")

funcion2_pruebas()

#--------------------------------------------------------------------------------

#SECCION DEL MENU

def menu():
    opcion = " "
    while opcion.upper() != "S" :
        print("")
        print("Bienvenido al sistema de convertidor de bases")
        print("")
        print("   Eliga una opcion:")
        print("")
        print("   1.  De base 10 a cualquier base(2 a 9)")
        print("   2.  De cualquier base a base 10")               
        print("   S.  Salir")
        print("")
        opcion = input("   Digite la opcion y presione ENTER -->")
        print("")
        if opcion == "1" :
            numero=int(input('Digite un numero en base 10:'))
            base=int(input('Digite la base a la que desea convertir el numero:'))
            print('El numero en base',base,"es -->",funcion1(numero,base))
            print("")
            print("")
        elif opcion == "2" :
            numero=int(input('Digite un numero que NO este en base 10:'))
            base=int(input('Digite la base del numero dado:'))
            print('El numero dado en base 10 es -->',funcion2(numero,base))
            print("")
            print("")
        else :
            print("Fin del programa")
            print("Roberto Garita, all rights reserved")       
menu()
