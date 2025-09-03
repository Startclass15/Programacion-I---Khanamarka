#Eje1. Clase Persona
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def mostrarInfo(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.carrera=carrera
    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} - Edad: {self.edad} - Carrera: {self.carrera}")

class Docente(Persona):
    def __init__(self,nombre,edad,materia):
        super().__init__(nombre,edad)
        self.materia=materia
    def mostrarInfo(self):
        print(f"Docente: {self.nombre} - Edad: {self.edad} - Materia: {self.materia}")

estudiante1=Estudiante("Kevin",29,"Sistemas Informaticos")
docente1=Docente("Kevin Arroyo",29,"Programación I")

estudiante1.mostrarInfo()
docente1.mostrarInfo()

#Ejercicio2. CLASE AUTOMOVIL

class Automovil():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def informacion(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo}")

class AutomovilElectrico(Automovil):
    def __init__(self, marca, modelo, capacidad_bateria):
        super().__init__(marca, modelo)
        self.capacidad_bateria=capacidad_bateria
    def informacion(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Capacidad Carga: {self.capacidad_bateria} kWh")

class AutomovilGasolina(Automovil):
    def __init__(self, marca, modelo, capacidad_tanque):
        super().__init__(marca, modelo)
        self.capacidad_tanque=capacidad_tanque
    def informacion(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Capacidad Tanque: {self.capacidad_tanque} L")

#EJ3. CLASE FIGURAS GEOMETRICAS
class FigurasGeometricas:
    def area(self):
        pass

class Cuadrado(FigurasGeometricas):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        return self.lado*self.lado

class Rectangulo(FigurasGeometricas):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    
#Eje4. clase cuenta bancaria
class CuentaBancaria:
    def __init__(self,titular, saldo=0):
        self.titular=titular
        self.saldo=saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
    def intereses(self,tasa=0.04):
        self.saldo=self.saldo+(self.saldo*tasa)
        return self.saldo

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite=limite
    def giros(self,monto):
        if self.saldo-monto>=-self.limite:
            self.saldo=self.saldo-monto
            print(f"Se giro {monto} - Nuevo saldo: {self.saldo}")
        else:
            print("Error no se puede exceder el limite")

#Ej 5. clase dispositivo
class Dispositivo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

class Celular(Dispositivo):
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)
        self.sistema_operativo=sistema_operativo
    def mostrarInfor(self):
        print(f"Celular {self.marca} - Modelo: {self.modelo} - SO: {self.sistema_operativo}" )

class Computadora(Dispositivo):
    def __init__(self, marca, modelo,procesador):
        super().__init__(marca, modelo)
        self.procesador=procesador
    def mostrarInfor(self):
        print(f"Computadora {self.marca} - Modelo: {self.modelo} - Procesador: {self.procesador}" )


#Ej6. Clase Empleado
class Empleado:
    def __init__(self,nombre,salario_base):
        self.nombre=nombre
        self.salario_base=salario_base

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)
    def calcularSalario(self):
        return self.salario_base+(self.salario_base*0.20)

class EmpleatoPorHoras(Empleado):
    def __init__(self, nombre, salario_base,horas_trabajadas):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas=horas_trabajadas
    def calularSalario(self):
        return self.horas_trabajadas*50
    
#Ej7. clase Vehiculo
class Vehiculo:
    def __init__(self):
        pass

class Bicicleta(Vehiculo):
    def mostrar(self):
        print("Bicicleta avanzando...")
class Auto(Vehiculo):
    def mostrar(self):
        print("Auto avanzando...")
class Avion(Vehiculo):
    def mostrar(self):
        print("Avion despegando...")

vehiculos=[Bicicleta(),Auto(),Avion()]
for recorrido in vehiculos:
    recorrido.mostrar()

#Eje 8. class tienda
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

class Carrito:
    def __init__(self):
        self.productos=[]
    def agregarProductos(self,producto):
        self.productos.append(producto)
    
    def mostrarProductos(self):
        total=0
        for i in self.productos:
            print(f"{i.nombre} - {i.precio} Bs")
            total=total+i.precio
        print(f"Total a pagar: {total}Bs")

class Alimento(Producto):
    def __init__(self, nombre, precio,fechaVencimiento):
        super().__init__(nombre, precio)
        self.fechaVencimiento=fechaVencimiento
class Electrodomesticos(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia=garantia


#Eje 9. clase biblioteca
class Libro:
    def __init__(self,titulo,autor,año_publicacion):
        self.titulo=titulo
        self.autor=autor
        self.año_publicacion=año_publicacion
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion,tamañoMB):
        super().__init__(titulo, autor, año_publicacion)
        self.tamañoMB=tamañoMB
    
    def descargar(self):
        print(f"Descargando el libro {self.titulo}....")

class LibroFisico(Libro):
    def __init__(self, titulo, autor, año_publicacion,ubicacion):
        super().__init__(titulo, autor, año_publicacion)
        self.ubicacion=ubicacion
    def prestar(self):
        print(f"El libro {self.titulo} ha sido prestado....")

#Eje 10 clase transporte publico

class Transporte:
    def __init__(self,origen,destino,costoBase):
        self.origen=origen
        self.destino=destino
        self.costoBase=costoBase

class Bus(Transporte):
    def __init__(self, origen, destino, costoBase, numeroAsientos):
        super().__init__(origen, destino, costoBase)
        self.numeroAsientos=numeroAsientos
    def calcular(self,ocupados):
        recargo=(ocupados/10)*2
        return self.costoBase+recargo
    
class Tren(Transporte):
    def __init__(self, origen, destino, costoBase, vagones):
        super().__init__(origen, destino, costoBase)
        self.vagones=vagones
    def calcular(self):
        return self.costoBase*self.vagones   