# Emmanuel andres chan yah
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()  

calificaciones = []

for i in range(5):
    entrada = simpledialog.askstring("Entrada", f"Captura la calificación {i+1}:")
    calificacion = int(entrada)  
    calificaciones.append(calificacion)  

resultado = "Calificaciones capturadas:\n"
for cal in calificaciones:
    resultado += str(cal) + "\n"

messagebox.showinfo("Resultados", resultado)
\
root.destroy()
