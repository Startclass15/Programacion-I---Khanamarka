#Ejercicio 1. -- 05/06/2025
#Calculadora 
#acciones sumar, restar, dividir, multiplicar =>funciones
class Calculadora:
    def __init__(self):
        pass
    #Acciones o metodos
    def sumar(self,a,b):
        return a+b
    def restar(self,x,y):
        return x-y
    def multiplicar(self,a,b):
        return a*b
    def dividir(self,a,b):
        return a/b

#EJE SUBCLASE CALCULADORA CIENTIFICA
#class CaCientifica(Calculadora):

#Objetos de la clase Calculadora

calculadora=Calculadora()

print("Calculadora Simple")

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=input("Seleccion la operacion que desea realizar: ")
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    if opcion=="1":
        print(f"La suma de {num1}+{num2}={calculadora.sumar(num1,num2)}")
    elif opcion=="2":
        print(f"La resta de {num1}-{num2}={calculadora.restar(num1,num2)}")
    elif opcion=="3":
        print(f"La multiplicacion de {num1}x{num2}={calculadora.multiplicar(num1,num2)}")
    elif opcion=="4":
        print(f"La division de {num1}/{num2}={calculadora.dividir(num1,num2)}")
    elif opcion=="5":
        print("Gracias por utilizar la calculadora....")
        break
    else:
        print("Error opcion invalida")
