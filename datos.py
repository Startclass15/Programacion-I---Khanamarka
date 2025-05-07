#Tipos de datos en Python
#Tipos de datos Simples
#Numericos (entero o decimales)
numero1=15.5
numero2=4
a=78
b=96
c=1.5

#Caracteres ("ABJKSHKJD1515")
nombre="Kevin"
x="5"
e='Programacion I'

#Boleanos (True/False)
xx=True
yy=False
prender=False

#Tipos de datos Complejos
#LISTAS Conjunto de datos ordenados o desordenados []
colores=["Rojo","Verde","Azul","Cafe"]
lista=[1,2,5,"Uno",True,1.5]
#NOTA: listas son mutables (se pueden modificar en el transcurso del codigo)

#TUPLAS
#La tuplas son un conjunto de datos ordenados o desordeados pero que no se pueden modificar
#Son datos inmutables (Una vez que se definen ya no se pueden modificar) ()
colores2=("Amarrillo","Rosado","Anaranjado")


#DICCIONARIOS 


#Ejercicio 1. Sumar 2 numero y mostrar el resultado
#PASO 1. DEFINIR LAS VARIABLES
num1=45.5
num2=7
suma=num1+num2
#Para escribir en pantalla (print())
print(suma)


#Ejercicio 2. Calcular la resta de 2 numeros y mostrar el resultado
r=78.4512
z=15.78941
restar=r-z
print(restar) 


#Leer datos por teclado 
#input() 
#Nota: input recepciona todo dato ya sea numerico o caracter como valor cadena de caracteres
#Para leer valores numericos se debe agregar al cual dato se convertira
#entero int(input())
#decimal float(input())
numeroDato=int(input("Ingrese un numero: "))
numeroDato2=int(input("Ingrese un numero: "))
sumar=numeroDato+numeroDato2
print(sumar)



