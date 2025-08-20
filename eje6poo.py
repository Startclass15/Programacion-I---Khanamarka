#Eje. Subclases 19/08/2025
#Representar la clase animal
#Y crear las subclases animales domesticos, animales salvajes

class Animal():
    def __init__(self,edad,especie,tamaño,sonido,color):
        self.edad=edad
        self.especie=especie
        self.tamaño=tamaño
        self.sonido=sonido
        self.color=color
    def dormir(self):
        print("Esta durmiendo...")
    def comer(self,comida):
        print("Esta comiendo ",comida)
    def moverse(self):
        print("Se esta moviendo...")

#subclase (animalesDomesticos)
class AnimalDomestico(Animal):
    def __init__(self,edad,especie,tamaño,sonido,color,nombre,raza,dueño,vacunas):
        #Heredar los atributos de la clase PADRE
        super().__init__(edad,especie,tamaño,sonido,color)
        self.nombre=nombre
        self.raza=raza
        self.dueño=dueño
        self.vacunas=vacunas
    #Acciones de la subclase
    def jugar(self):
        print("Esta jugando con ", self.dueño)

#Objetos de clase Animal Domesticos
perro=AnimalDomestico(5,"perro","30cm","Ladrar","Blanco","Scott","Criollo","Kevin Arroyo","parvovirus,rabia,abc")
perro.comer("Carne")
perro.jugar()
perro.moverse()


#subclase animales salvajes
class AnimalSalvaje(Animal):
    def __init__(self,edad,especie,tamaño,sonido,color,habitad,zonaGeografica,nivelPeligrosidad):
        #Heredar los atributos de la clase padre
        super().__init__(edad,especie,tamaño,sonido,color)
        self.habitad=habitad
        self.zonaGeografica=zonaGeografica
        self.nivelPeligrosidad=nivelPeligrosidad
    def cazar(self):
        print("Esta cazando su comida...")
        comida=input("Que cazo? ")
        return comida
    def explorar(self):
        print("Esta explorando nuevas areas...")

leon=AnimalSalvaje(2,"Felino","2.1m","ruge","naranja","selva","Africa","Muy Peligroso")
leon.comer(leon.cazar())
leon.dormir()
leon.explorar()
leon.moverse()