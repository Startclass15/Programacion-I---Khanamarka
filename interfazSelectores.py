#Tipos de selectores y listas para interfaz
#1. ListBox: Lista de elementos
#2. Checkbutton: Casillas de verificacion
#3. RadioButton: Botones de opciones "solo se puede elegir una sola opcion"

import tkinter as tk

ventana=tk.Tk()
ventana.title("Selectores y Listas")
ventana.geometry("300x600")

#Crear la lista
lista=tk.Listbox(ventana,
                 selectmode=tk.MULTIPLE,
                 bg="#7AF2AC",
                 fg="#000",
                 font=("Arial", 16, "bold"),
                 selectbackground="#CF52F5"  
                 )
#Opciones de la lista
opciones=["Rojo","Verde","Azul","Amarillo","Cafe","Rosado","Lila","Blanco"]

for color in opciones:
    lista.insert(tk.END, color)

lista.pack()

rojo=tk.BooleanVar()
azul=tk.BooleanVar()
amarillo=tk.BooleanVar()
verde=tk.BooleanVar()

#CASILLAS DE VERIFICICACION
opcion1=tk.Checkbutton(ventana, text="Rojo", variable=rojo, 
                       font=("Arial",16,"bold"))
opcion2=tk.Checkbutton(ventana,text="Azul", variable=azul,font=("Arial",16,"bold"))
opcion3=tk.Checkbutton(ventana,text="Amarillo",variable=amarillo,font=("Arial",16,"bold"))
opcion4=tk.Checkbutton(ventana,text="Verde", variable=verde,font=("Arial",16,"bold"))
opcion1.pack()
opcion2.pack()
opcion3.pack()
opcion4.pack()

#RADIO  Botones

lenguajeProgramacion=tk.StringVar()
a=tk.Radiobutton(ventana,text="Python", variable=lenguajeProgramacion, value="Python",
                 font=("Arial",16,"bold"))
b=tk.Radiobutton(ventana,text="Java", variable=lenguajeProgramacion, value="Java",font=("Arial",16,"bold"))
c=tk.Radiobutton(ventana,text="Kotlin",variable=lenguajeProgramacion, value="Kotlin",font=("Arial",16,"bold"))
d=tk.Radiobutton(ventana,text="JavaScript",variable=lenguajeProgramacion, value="JavaScript",font=("Arial",16,"bold"))
a.pack()
b.pack()
c.pack()
d.pack()


ventana.mainloop()