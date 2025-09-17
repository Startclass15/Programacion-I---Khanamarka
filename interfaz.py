#Tkinter: es una libreria para interfaces graficas

#IMPORTACION DE LA LIBRERIA
#PASO 1. IMPORTAR LA LIBRERIA tkinter
import tkinter as tk
from tkinter import PhotoImage

#PASO 2. CREACION DE UNA VENTANA (tk.Tk())
ventana=tk.Tk()
ventana.title("Primera Interfaz")
ventana.geometry("300x600")

#AGREGAR UN TEXTO A LA PANTALLA
titulo=tk.Label(ventana,text="KEVIN ARROYO MONTAÑO", font=("Arial",16))
titulo.pack() #Posicionamineto del componente
#BOTONES
def click():
    print("Hola bienvenido...")
#boton=tk.Button(contenedor,opciones)
boton=tk.Button(
    ventana, #contenedor 
    text="Seleccionar", #Texto del boton
    background="#22BFCA", #Fondo del boton
    command=click, #El accionante click
    font=("Arial",14,"bold"), #Estilos del texto del boton
    fg="white", #Color del texto del boton
    width=20, #Ancho del Boton
    height=1, #Alto del boton
    state="normal", #Estado del boton
    relief="flat"
    ) #
boton.pack()
boton2=tk.Button(
    ventana, #contenedor 
    text="Seleccionar", #Texto del boton
    background="#22CAA3", #Fondo del boton
    command=click, #El accionante click
    font=("Arial",14,"bold"), #Estilos del texto del boton
    fg="white", #Color del texto del boton
    width=20, #Ancho del Boton
    height=1, #Alto del boton
    state="normal", #Estado del boton
    relief="raised",
    bd=8
    ) 
boton2.pack()

#Botones tipo imagenes (image)
#importar la libreria de imagenes
imagen=PhotoImage(file="pyt.png")
botonImagen=tk.Button(
    ventana,
    image=imagen,
    relief="raised",
    text="Python",
    compound="bottom",
    font=("Arial",16,"bold")
)
botonImagen.pack()


#PASO 3 INICIALIZAR LA VENTANA
ventana.mainloop()
