#Plantilla para bucle for
#for variableIteracion in range(valorInicial,valorFinal,incremento):
#CREAR EL PROGRAMA QUE MUESTRE LA TABLA DE MULTIPLICAR DEL 9
for tabla9 in range(1,11,1):
    print(tabla9,"x3=",tabla9*3)


#tabla de multiplicar de cualquier numero ingresado por teclado
numero=int(input("Ingrese un numero para la tabla de multiplicar: "))
for tablaN in range(1,11,1):
    print(tablaN,"x",numero,"=",tablaN*numero)