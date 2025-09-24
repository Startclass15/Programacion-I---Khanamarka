from tkinter import *

ventana=Tk()
ventana.title("Entradas de datos")
ventana.geometry("400x250")

#TIPO DE DATOS
numero2=DoubleVar()
numero=IntVar()
nombre2=StringVar()
encender=BooleanVar()

#Componente para entrada de datos 
Entry(ventana,
             textvariable=numero,
             font=("Arial",16,"bold"), #estilos del texto
             fg="red", #color de texto
             bg="yellow", #color de fondo
             width=20, #ancho
             justify="center", #alineacion
             bd=3, #grosor bordeado
             cursor="xterm", #cursor
             selectbackground="black", #color al seleccionar
             insertbackground="red", #color al insertar
             selectforeground="green", #color de la letras al seleccionar
             #show="*" #CONTRASEÑAS

             ).pack()
Entry(ventana,textvariable=numero2).pack()
Entry(ventana,textvariable=nombre2).pack()
Entry(ventana,textvariable=encender).pack()

def mostrarDatos():
    print("datos: ",numero.get(),type(numero.get()))
    print("datos: ",numero2.get(),type(numero2.get()))
    print("datos: ",nombre2.get(),type(nombre2.get()))
    print("datos: ",encender.get(),type(encender.get()))

Button(ventana,text="Mostrar",command=mostrarDatos).pack()


ventana.mainloop()