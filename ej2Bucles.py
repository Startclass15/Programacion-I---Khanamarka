#Mostrar los numero primos 100
#2,3,5,7,11,13....

for primos in range(2,201,1):
    numeroPrimo=True
    for verificador in range(2,int(primos**0.5)+1):
        #condicion
        if primos % verificador==0:
            numeroPrimo=False
            break
    if numeroPrimo:
        print(primos)
