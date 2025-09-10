#Tkinter: es una libreria para interfaces graficas

#IMPORTACION DE LA LIBRERIA
#PASO 1. IMPORTAR LA LIBRERIA tkinter
import tkinter as tk

#PASO 2. CREACION DE UNA VENTANA (tk.Tk())
ventana=tk.Tk()
ventana.title("Primera Interfaz")
ventana.geometry("200x400")

#AGREGAR UN TEXTO A LA PANTALLA
titulo=tk.Label(ventana,text="Primera Interfaz")
titulo.pack() #Posicionamineto del componente

#PASO 3 INICIALIZAR LA VENTANA
ventana.mainloop()
