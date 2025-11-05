import tkinter as tk

def mostrar():
    nombreCompleto=nombre.get()+" "+ apellido.get()
    resultado.config(text="Nombre Completo: "+nombreCompleto)

ventana=tk.Tk()
ventana.title("Ejercicio 2")
ventana.geometry("400x300")

nombre=tk.Entry(ventana)
nombre.pack()

apellido=tk.Entry(ventana)
apellido.pack()

boton=tk.Button(ventana,text="Mostrar", command=mostrar)
boton.pack()

resultado=tk.Label(ventana, text="")
resultado.pack()


ventana.mainloop()