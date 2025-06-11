#Crear un bucle iterativo para recibir 5 notas de estudiantes
#y calcular la nota final
totalNota=0
for nota in range(1,6,1):
    print("Ingrese la nota",nota,"=")
    notas=int(input())
    totalNota=totalNota+notas

notaFinal=totalNota/5
print("La nota Final es ",notaFinal)