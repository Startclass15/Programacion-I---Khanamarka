#Ejercicio 2. POO. CREAR LA CLASE RECTANGULO
#PARAMETROS (ancho,alto)
#Acciones, (CALCULAR EL AREA) - CALCULAR EL VOLUMEN, CALCULAR EL PERIMETRO 
class Rectangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto

    #acciones o metodos
    def area(self):
        return self.ancho*self.alto
    def volumen(self):
        print("PARA CALCULAR EL VOLUMEN SE NECESITA LA PROFUNDIDAD. PRISMA...")
    def perimetro(self):
        return (self.ancho+self.alto)*2

#Paso4. Objetos de la clase rectangulo
ancho=int(input("Ingrese el ancho del rectangulo. "))
alto=int(input("Ingrese el alto del rectagulo. "))
rectangulo1=Rectangulo(ancho,alto)
print(f"El area del rectangulo es {rectangulo1.area()}")
print("El perimetro del rectangulo es ",rectangulo1.perimetro() )
rectangulo1.volumen()