#Realizar un programa que solicite 3 notas y calcule el promedio
#para luego verificar si el estudiante aprobo o reprobo
#51 nota minima de aprobacion
nota1=int(input("Ingrese una nota: "))
nota2=int(input("Ingrese una nota: "))
nota3=int(input("Ingrese una nota: "))
promedio=(nota1+nota2+nota3)/3
if promedio>=51:
    print("Aprobado con ",promedio)
else:
    print("Reprobado con ",promedio)
