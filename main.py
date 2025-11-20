from Datos import Datos 
from GestionDatos import GestionDatos

gd=GestionDatos
dt=Datos
#clase datos gestion datosnombre apellido edad correo, documento par constructor e impar por set y get
menuActivo=True
while menuActivo:
    #Se realiza un menu para verifica las funciones
    print("1. Agregar")
    print("2. Consultar")
    #print("3. Ver lista")
    print("4. Salir")
    #Se solicita que ingrese la opcion que va a elegir
    opcion=input("Ingrese una opcion: ")

    if opcion == "1":
        dt=Datos()
        dt.nombre = str(input("Ingrese su nombre: "))
        dt.apellido = str(input("Ingrese su apeellido: "))
        dt.cedula = int(input("Ingrese su numero de cedula: "))
        dt.correo = str(input("Ingrese su correo: "))
        dt.edad = int(input("Ingrese su edad: "))
        gd=GestionDatos()
        gd.lista.append(dt)
        gd.lista=gd.lista
    elif opcion == "2":
        print(gd.lista)
        cedula = input("Ingrese numero de cedula para la Consulta: ")
        result=gd.consultarDatos(cedula)
        print(result)

    # elif opcion == "3":
    #     print(gd.lista)

    elif opcion == "4":
        #Con esta opcion se sale del programa
        print("Saliendo del programa")
        
        

