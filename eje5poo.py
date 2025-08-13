#Ejercicio1. 12/08/2025
#Crear la clase padre Persona
#Crear las subclases Estudiante Docente

class Persona:
    def __init__(self,ci,nombre,edad):
        self.ci=ci
        self.nombre=nombre
        self.edad=edad
    #acciones
    def comer(self,comida):
        comida=input("Cual comida comera? ")
        print("Esta comiendo ",comida)
    def dormir(self):
        print("Esta durmiendo")

class Estudiante(Persona):
    def __init__(self,ci,nombre,edad,correo,codEstudiante,carrera):
        #Heredar las propiedades de la clase padre
        super().__init__(ci,nombre,edad)
        self.correo=correo
        self.codEstudiante=codEstudiante
        self.carrera=carrera
    def estudiar(self):
        print("Esta estudiando...")
    def darExamen(self):
        print("esta dando examen...")


estudiante1=Estudiante(7414554,"Kevin Arroyo",29,"k@gmail.com",745512,"Sistemas")

estudiante1.comer("Pan")
estudiante1.dormir()
estudiante1.estudiar()
estudiante1.darExamen()