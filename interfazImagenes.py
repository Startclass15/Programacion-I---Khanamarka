#IMAGENES EN TKINTER 
#1. IMAGENES EN UN LABEL from PIL import Image, ImageTk
#PILLOW SE DEBE INSTALAR
#pip install pillow

import tkinter as tk
from PIL import Image, ImageTk
import requests
import io

ventana=tk.Tk()
ventana.title("Imagenes")
ventana.geometry("350x500")

#Paso 1. Cargar con Pillow la imagen
rutaImagen=Image.open("source.gif")
imagen=ImageTk.PhotoImage(rutaImagen)
#tamaño=imagen(150,150)

#Paso 2. Mostrarlo en un label
#labelImagen=tk.Label(ventana, image=imagen)
#labelImagen.pack()

#Paso Extra usar con urls
url="https://bambu-mobile.com/wp-content/uploads/2022/07/Que-es-Python.png"
respuesta=requests.get(url)
respuesta.raise_for_status()

#Paso 2. Extra conversion de bytes a imagen
imagenBytes=io.BytesIO(respuesta.content)
imagenNueva=Image.open(imagenBytes)

imageTamaño=imagenNueva.resize((50,150),Image.LANCZOS)
imagenNueva2=ImageTk.PhotoImage(imagenNueva)



lableUrl=tk.Label(ventana,image=imagenNueva2)
lableUrl.pack()


ventana.mainloop()