#Ejercicio 1.
import tkinter as tk

ventana=tk.Tk()
ventana.title("Examen Tkinter")
ventana.geometry("400x300")
ventana.resizable(False,False)

label=tk.Label(ventana,text="Bienvenido al examen de Tkinter")
label.pack()


ventana.mainloop()