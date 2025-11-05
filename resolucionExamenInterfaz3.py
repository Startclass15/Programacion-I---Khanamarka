import tkinter as tk

contador=0

def aumentar():
    global contador
    contador=contador+1
    numero.config(text=str(contador))

def disminuir():
    global contador
    contador=contador-1
    numero.config(text=str(contador))


ventana=tk.Tk()
ventana.title("Ejercicio 3")
ventana.geometry("200x200")

numero=tk.Label(ventana,text=str(contador), font=("Arial",24,"bold"))
numero.pack()

boton1=tk.Button(ventana,text="+",command=aumentar)
boton1.pack()

boton2=tk.Button(ventana, text="-",command=disminuir)
boton2.pack()

ventana.mainloop()