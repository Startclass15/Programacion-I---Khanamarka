#Las condicionales Multiples se utiliza cuando se tiene mas de una condicion
#SINTAXIS
#if condicion
#elif condicion2
#elif condicion3
#else 

#Realizar un programa que calcule el promedio de las notas de un estudiante
#deberan ser 3 notas y verificar el estado
#ESTADO 1 MENOS 51 => REPROBADO
#ESTADO 2 DE 51 A 61 => REGULAR
#ESTADO 3 DE 61 A 71 => BIEN
#ESTADO 4 DE 71 A 81 => MUY BIEN
#ESTADO 5 DE 81 A 91 => EXCELENTE
#ESTADO 6 DE 91 A 100 => SOBRESALIENTE

nota1=int(input("Ingrese la nota: "))
nota2=int(input("Ingrese la nota: "))
nota3=int(input("Ingrese la nota: "))
notaFinal=(nota1+nota2+nota3)/3
if notaFinal>=91:
    print("Sobresaliente - Nota Final: ",notaFinal )
elif notaFinal>=81:
    print("Excelente - Nota Final: ",notaFinal)
elif notaFinal>=71:
    print("Muy Bien - Nota Final: ", notaFinal)
elif notaFinal>=61:
    print("Bien - Nota Final: ",notaFinal)
elif notaFinal>=51:
    print("Regular - Nota Final: ",notaFinal)
else:
    print("Reprobado - Nota Final: ",notaFinal)