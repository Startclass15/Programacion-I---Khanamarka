#Realizar un programa que verifique el mayor de tres numeros
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
c=int(input("Ingrese un numero: "))
if a==b==c:
    print("Los numeros son iguales")
else:
    if a>b:
        if a>c:
            print("El mayor es ",a)
        else:
            print("El mayor es ",c)
    else:
        if b>c:
            print("El mayor es ",b)
        else:
            print("El mayor es ",c)