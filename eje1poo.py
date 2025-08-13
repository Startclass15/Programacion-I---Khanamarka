#Eje1. POO. Crear la clase Persona
#clase Persona  atributos(Nombre, Edad, Ci)
class Persona():
    #Paso2. Definir el constructor para los atributos
    def __init__(self,nombre,edad,ci):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    #Paso 3. Definir las acciones o metodos
    def dormir(self):
        print(f"{self.nombre} esta durmiendo...")
    def comer(self,comida,lugar):
        print(f"{self.nombre} esta comiendo {comida} en {lugar}")
    def caminar(self):
        print(f"{self.nombre} esta caminando...")

#Paso 4. Definir los objetos de la clase Persona
persona1=Persona("Kevin Arroyo",29,1234567)
persona2=Persona("Juan",25,7451258)
persona3=Persona("Ana",26,4458812)
persona1.dormir()
persona2.comer("Pan","el colegio")
persona3.caminar()


