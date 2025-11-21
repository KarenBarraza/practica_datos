#se importa las clases necesarias
from Datos import Datos 
from GestionDatos import GestionDatos

#se crea el objeto de la clase GestionDatos
gd=GestionDatos()

#se crea un menu para interactuar con el usuario
menuActivo=True
while menuActivo:
    #Se realiza un menu para verifica las funciones
    print("No Registros: ", len(gd.lista))
    print("-------------------")
    print("Menu de opciones")
    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")
    #Se solicita que ingrese la opcion que va a elegir
    opcion=input("Ingrese una opcion: ")

    if opcion == "1":
        #Con esta opcion se agregan datos a la lista
        dt=Datos()
        dt.nombre = str(input("Ingrese su nombre: "))
        dt.apellido = str(input("Ingrese su apellido: "))
        dt.cedula = int(input("Ingrese su numero de cedula: "))
        dt.correo = str(input("Ingrese su correo: "))
        dt.edad = int(input("Ingrese su edad: "))
        gd.agregar_datos(dt)
    elif opcion == "2":
        #Con esta opcion se consultan datos de la lista
        cedula = int(input("Ingrese numero de cedula para la Consulta: "))
        result=gd.consultarDatos(cedula)
        print(result.nombre,result.apellido,result.edad,result.correo,result.cedula)
    elif opcion == "3":
        #Con esta opcion se sale del programa
        print("Saliendo del programa")
        
        

