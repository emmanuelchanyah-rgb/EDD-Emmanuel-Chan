# Importamos la librería necesaria para usar cuadros de diálogo
import tkinter as tk
from tkinter import simpledialog, messagebox

# Inicializamos la ventana principal de Tkinter (necesaria para los cuadros de diálogo)
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal para que solo se muestren los diálogos

# Creamos una lista vacía para guardar las calificaciones
calificaciones = []

# Ciclo para pedir 5 calificaciones
for i in range(5):
    entrada = simpledialog.askstring("Entrada", f"Captura la calificación {i+1}:")
    calificacion = int(entrada)  # Convertimos la entrada de texto a número entero
    calificaciones.append(calificacion)  # Guardamos en la lista

# Construimos el mensaje con todas las calificaciones capturadas
resultado = "Calificaciones capturadas:\n"
for cal in calificaciones:
    resultado += str(cal) + "\n"

# Mostramos las calificaciones en un cuadro de diálogo
messagebox.showinfo("Resultados", resultado)

# Cerramos la ventana de Tkinter
root.destroy()
