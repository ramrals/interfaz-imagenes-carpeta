import tkinter as tk
from PIL import ImageTk, Image
import os

def cargar_imagenes(carpeta):
    imagenes = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            ruta = os.path.join(carpeta, archivo)
            imagen = Image.open(ruta)
            imagen = imagen.resize((200, 200), Image.ANTIALIAS)
            imagen = ImageTk.PhotoImage(imagen)
            imagenes.append(imagen)
    return imagenes

def mostrar_imagenes():
    carpeta = "ruta_de_la_carpeta"
    imagenes = cargar_imagenes(carpeta)
    
    ventana = tk.Tk()
    ventana.title("Cargar imágenes")
    
    for imagen in imagenes:
        etiqueta = tk.Label(ventana, image=imagen)
        etiqueta.pack()
    
    ventana.mainloop()

mostrar_imagenes()
