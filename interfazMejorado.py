#Interfaz mejorada de Bootstrap Tkinter

#TEMAS PARA CONFIGURAR
#1. MODO CLARO
# flatly: Azul Moderno
#litera: Blacn con azul claro
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
titulo.pack(pady=15)

boton=ttk.Button(ventana,text="Prueba boton")
boton.pack(pady=10)

#PASO 3. INICIALIZAR LA VENTANA
ventana.mainloop()

