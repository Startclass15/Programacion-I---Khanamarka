#SINTAXIS BASICA DE LAS FUNCIONES
#FUNCION => def nombreFuncion(parametros):
#retorno => return 

#Tipos de Funciones
#Funciones con parametros
#ej1. Funcion para sumar 2 numeros
def sumar(num1,num2):
    return num1+num2

#Como utilizar una funcion
resultado=sumar(7,3)
print(resultado)

print(sumar(8,15))
print(sumar(9,6))


#funcion para restar 2 numeros
def restar(a,b):
    return a-b


def multiplicar(a,b):
    return a*b


def dividir(a,b):
    return a/b

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
print(a,"+",b,"=",sumar(a,b))
print(a,"-",b,"=",restar(a,b))
print(a,"x",b,"=",multiplicar(a,b))
print(a,"/",b,"=",dividir(a,b))


#Ej1. Crear una funcion para calcular el area del circulo
def areaCirculo(radio):
    return 3.1416*radio*radio

radio=int(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ",areaCirculo(radio))


#Ej2. Crear una funcion para calcular el area del rectangulo
def areaRectangulo(base,altura):
    return base*altura

base=int(input("Ingrese la base del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))
print("El area del rectangulo es: ",areaRectangulo(base,altura))



#Funciones sin parametros