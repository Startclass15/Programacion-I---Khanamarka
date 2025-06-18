#Funcions sin parametros
#Funcion para controlar acciones
#Con condicionales y bucles


def MenuOpciones():
    while True:
        print("Menu de Opciones")
        print("1. Opcion 1")
        print("2. Opcion 2")
        print("3. Opcion 3")
        print("4. Opcion 4")
        print("5. Salir")
        opcion=input("Elija una opcion: ")
        if opcion=="1":
            print("Se eligio la opcion 1")
        elif opcion=="2":
            print("Se eligio la opcion 2")
        elif opcion=="3":
            print("Se eligio la opcion 3")
        elif opcion=="4":
            print("Se eleigio la opcion 4")
        elif opcion=="5":
            print("Gracias utilizar el programa...")
            return False
        else:
            print("Opcion Invalida")


MenuOpciones()