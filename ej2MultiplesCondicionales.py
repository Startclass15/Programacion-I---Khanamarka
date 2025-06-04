#Ej2. crear un programa que muestre el dia basado en el numero ingresado
#ejemplos si ingresamos 2 debera mostrar MARTES
#1 LUNES
#2 MARTES
#3 MIERCOLES
#4 JUEVES 
#5 VIERNES
#6 SABADO
#7 DOMINGO
dia=int(input("Ingrese un numero del 1 al 7: "))
if dia==1:
    print("LUNES")
elif dia==2:
    print("MARTES")
elif dia==3:
    print("MIERCOLES")
elif dia==4:
    print("JUEVES")
elif dia==5:
    print("VIERNES")
elif dia==6:
    print("SABADO")
elif dia==7:
    print("DOMINGO")
else:
    print("Error numero no valido")