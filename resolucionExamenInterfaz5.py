import tkinter as tk

def sumar():
    num1=float(numero1.get())
    num2=float(numero2.get())
    res=num1+num2
    resultado.config(text=res)

def restar():
    num1=float(numero1.get())
    num2=float(numero2.get())
    res=num1-num2
    resultado.config(text=res)

def multiplicar():
    num1=float(numero1.get())
    num2=float(numero2.get())
    res=num1*num2
    resultado.config(text=res)

def dividir():
    num1=float(numero1.get())
    num2=float(numero2.get())
    res=num1/num2
    resultado.config(text=res)


ventana=tk.Tk()
ventana.title("Ejercicio 5")
ventana.geometry("400x300")

tk.Label(ventana,text="Ingrese el numero 1: ").pack()
numero1=tk.Entry(ventana)
numero1.pack()

tk.Label(ventana,text="Ingrese el numero 2: ").pack()
numero2=tk.Entry(ventana)
numero2.pack()

suma=tk.Button(ventana,text="SUMAR",command=sumar)
suma.pack()
resta=tk.Button(ventana,text="RESTAR",command=restar)
resta.pack()
multiplica=tk.Button(ventana,text="MULTIPLICAR",command=multiplicar)
multiplica.pack()
divide=tk.Button(ventana,text="DIVIDIR",command=dividir)
divide.pack()

resultado=tk.Label(ventana,text="0",font=("Arial",20,"bold"))
resultado.pack()



ventana.mainloop()