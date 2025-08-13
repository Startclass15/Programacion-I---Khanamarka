#INTRODUCCION A LA PROGRAMACION ORIENTADA A OBJETOS
#CLASES => class
#PROPIEDADES (NOMBRE, EDAD, CARRERA, CI)
#METODOS => def (funciones)
#OBJETOS

#ejemplo 1. clase Estudiante
#LAS CLASES SE DEFINEN CON LA PRIMERA LETRA MAYUSCULA
class Estudiante:
    #DEFINIR LAS PROPIEDADES
    def __init__(self,nombre,edad,carrera,ci):
        #El "self" es una referenciador al objeto
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        self.ci=ci
    
    #DEFINIR LAS ACCIONES O METODOS DE LA CLASE (estudiar)
    #nota las acciones se definen como funciones (def)
    def estudiar(self): #funcion sin parametro
        print("Esta estudiando...")
    
    def comer(self,comida): #funcion con parametro
        print("esta comiendo ",comida)


edson=Estudiante("Edson",25,"Sistemas Informaticos",1234567)
liborio=Estudiante("Liborio",26,"Sistemas Informaticos",78784465)

liborio.estudiar()
edson.comer("Pan")

#NOTA LOS OBJETOS DE UNA CLASE SE CREAN POR FUERA DE LA CLASE