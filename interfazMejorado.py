#Interfaz mejorada de Bootstrap Tkinter

#TEMAS PARA CONFIGURAR
#1. MODO CLARO
# flatly: Azul Moderno
#litera: Blanco con azul claro
#minty: verde
#pulse: blanco con morado
#united: naranja

#2 MODO OSCURO
#darkly: gris oscuro con azul
#cyborg: negro con turquesa
#solar: negro con dorado
#superhero: negro azulado
#vapor: magenta

#PASO 1. IMPORTACION DE LA LIBRERIA
import ttkbootstrap as ttk


#PASO 2. CREAR LA VENTANA
ventana=ttk.Window(themename="vapor")
ventana.title("Mejora Interfaz")
ventana.geometry("300x300")

titulo=ttk.Label(ventana,text="Intefaz Bootstrap", font=("Arial",20,"bold"))
titulo.grid(column=2,row=0,pady=15)

boton=ttk.Button(ventana,text="Prueba boton")
boton.grid(row=0,column=3,pady=10)


#Checbuttom, RadioBox, ComoboBox
opcion1=ttk.Checkbutton(ventana,text="Opcion 1")
opcion1.grid(pady=10,row=1,column=3)
opcion2=ttk.Checkbutton(ventana,text="Opcion 2")
opcion2.grid(pady=10,row=1,column=4)

radio1=ttk.Radiobutton(ventana,text="Opcion 1 radio")
radio1.grid(pady=10,row=3,column=3)

opciones=["Opcion1","Opcion2","Opcion3","Opcion4"]
conjunto=ttk.Combobox(ventana,values=opciones)
conjunto.grid(row=4,column=3)

titulo1=ttk.Label(ventana,text="Prueba")
titulo1.grid(row=4,column=1)


dato=ttk.Checkbutton(ventana,text="Prueba")
dato.grid(column=0,row=2)

#Posicionamientos

#Vertical pack()
#Filas, columnas grid()

#PASO 3. INICIALIZAR LA VENTANA
ventana.mainloop()

