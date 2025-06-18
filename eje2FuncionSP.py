#Funcion sin parametros para crear una calculadora basica
def calculadora():
    while True:
        print("Menu de Opciones")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion=input("Elija una opcion: ")
        if opcion=="1":
            a=int(input("Ingrese un numero: "))
            b=int(input("Ingrese un numero: "))
            suma=a+b
            print(f"La suma de {a}+{b}={suma}")
        elif opcion=="2":
            a=int(input("Ingrese un numero: "))
            b=int(input("Ingrese un numero: "))
            resta=a-b
            print(f"La resta de {a}-{b}={resta}")
        elif opcion=="3":
            a=int(input("Ingrese un numero: "))
            b=int(input("Ingrese un numero: "))
            multiplicar=a*b
            print(f"La multiplicacion de {a}x{b}={multiplicar}")
        elif opcion=="4":
            a=int(input("Ingrese un numero: "))
            b=int(input("Ingrese un numero: "))
            division=a/b
            print(f"La division de {a}/{b}={division}")
        elif opcion=="5":
            print("Gracias utilizar la calculadora...")
            return False
        else:
            print("Opcion Invalida")

calculadora()