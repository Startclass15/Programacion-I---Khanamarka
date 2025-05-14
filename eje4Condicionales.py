#Realizar un programa que solicite tres lados de un triangulo
#verificar el tipo de triangulo que es 

#nota TRIANGULO EQUILATERO 3 LADOS IGUALES
#TRIANGULO ISOCELES 2 LADOS IGUALES
#TRIANGULO ESCALENO 3 LADOS DIFERENTES

#PASO 1. OBTENER LOS LADOS DEL TRIANGULO
lado1=float(input("Ingrese el primer lado: "))
lado2=float(input("Ingrese el segundo lado: "))
lado3=float(input("Ingrese el tercer lado: "))

if lado1==lado2==lado3:
    print("El triangulo es equilatero")
else:
    if lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("El triangulo es Isoceles")
    else:
        print("Es un triangulo escaleno")
