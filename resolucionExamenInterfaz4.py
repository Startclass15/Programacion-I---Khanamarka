import tkinter as tk

def cambiarColor():
    color=opcion.get()
    cambioColor.config(fg=color)

ventana=tk.Tk()
ventana.title("Ejercicio 4")
ventana.geometry("400x250")

opcion=tk.StringVar(value="negro")
opcion1=tk.Radiobutton(ventana,text="Rojo", variable=opcion, value="red", command=cambiarColor)
opcion1.pack()
opcion2=tk.Radiobutton(ventana,text="Verde", variable=opcion, value="green",command=cambiarColor)
opcion2.pack()
opcion3=tk.Radiobutton(ventana,text="Azul",variable=opcion, value="blue",command=cambiarColor)
opcion3.pack()

cambioColor=tk.Label(ventana,text="Ejercicio 4", font=("Arial",25,"bold"))
cambioColor.pack()


ventana.mainloop()