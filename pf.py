import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import pyttsx3
from google import genai

# Inicializa cliente Gemini
client = genai.Client(api_key="AIzaSyD49PkW0485GBcQqFR6hZHk3twSlhutEsA")
MODEL_NAME = "gemini-2.5-flash-lite-preview-09-2025"

# Inicializa motor de voz
voz = pyttsx3.init()

# ---- Función para hablar ----
def hablar(texto):
    voz.say(texto)
    voz.runAndWait()

# ---- Función para obtener respuesta de Gemini ----
def obtener_respuesta(texto_usuario):
    try:
        prompt = (
            "Eres un amigo empático que brinda apoyo emocional a estudiantes con estrés. "
            "Da respuestas cortas, positivas y tranquilizadoras.\n\n"
            f"Estudiante: {texto_usuario}\nAmigo:"
        )
        respuesta = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        print(respuesta)
        texto = getattr(respuesta, "text", "No logré obtener respuesta.")
        return texto
    except Exception as e:
        return f"Error al conectar: {e}"

# ---- Función de envío ----
def enviar():
    mensaje = entrada.get().strip()
    if not mensaje:
        return
    entrada.delete(0, tk.END)

    chat.config(state="normal")
    chat.insert(tk.END, f"Tú: {mensaje}\n", "user")
    chat.config(state="disabled")

    respuesta = obtener_respuesta(mensaje)
    chat.config(state="normal")
    chat.insert(tk.END, f"Amigo: {respuesta}\n\n", "bot")
    chat.config(state="disabled")
    chat.yview(tk.END)

    hablar(respuesta)

# ---- Interfaz con ttkbootstrap ----
app = ttk.Window(themename="superhero")
app.title("🤖 Amigo del Estrés")
app.geometry("650x450")

titulo = ttk.Label(app, text="Amigo del Estrés 💬", font=("Helvetica", 18, "bold"))
titulo.pack(pady=10)

chat = tk.Text(app, wrap="word", state="disabled", height=15, width=70, bg="#f8f9fa", fg="#212529", font=("Arial", 11))
chat.tag_config("user", foreground="#0d6efd", font=("Arial", 11, "bold"))
chat.tag_config("bot", foreground="#198754", font=("Arial", 11))
chat.pack(padx=10, pady=10, fill=BOTH, expand=True)

frame = ttk.Frame(app)
frame.pack(fill=X, padx=10, pady=5)

entrada = ttk.Entry(frame)
entrada.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))
entrada.bind("<Return>", lambda e: enviar())

boton = ttk.Button(frame, text="Enviar", bootstyle="success", command=enviar)
boton.pack(side=RIGHT)

# Mensaje inicial
chat.config(state="normal")
chat.insert(tk.END, "Amigo: Hola 👋 Soy tu amigo del estrés.\n"
                    "Cuéntame cómo te sientes y te ayudaré con calma y apoyo.\n\n", "bot")
chat.config(state="disabled")

app.mainloop()
