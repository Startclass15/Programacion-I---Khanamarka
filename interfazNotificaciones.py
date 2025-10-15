#Pantallas Emergentes 
#messagebox (ALERTAS, INFORMATIVOS, MENSAJES)
#1. INFORMACTIVO showinfo()
#2. ADVERTENCIA showwarning()
#3. ERROR showerror()
#4. PREGUNTA askquestion()
#5. RETORNO askyesno() Retorna si o no (true / false)

#INFORMATIVO showinfo()
import tkinter as tk
from tkinter import messagebox #Importacion de las alertas

def mostrarInfo():
    messagebox.showinfo("Informacion","Mensaje de Informacion")

def mostrarAdvertencia():
    messagebox.showwarning("Advertencia","Mensaje de advertencia")

def mostrarError():
    messagebox.showerror("Error","Mensaje de error")

def mostrarPregunta():
    messagebox.askquestion("Pregunta","Cual es su nombre?")

def mostrarRetorno():
    messagebox.askyesnocancel("Enviar","Desea enviar los datos?")

ventana=tk.Tk()
ventana.title("Notificaciones")
ventana.geometry("320x450")

boton=tk.Button(ventana, text="Mostrar Información", command=mostrarInfo)
boton.pack()
boton2=tk.Button(ventana, text="Mostrar Advertencia", command=mostrarAdvertencia)
boton2.pack()
boton3=tk.Button(ventana,text="Mostrar Error", command=mostrarError)
boton3.pack()
boton4=tk.Button(ventana,text="Mostrar Pregunta", command=mostrarPregunta,)
boton4.pack()
boton5=tk.Button(ventana,text="Mostrar Retorno", command=mostrarRetorno)
boton5.pack()



ventana.mainloop()