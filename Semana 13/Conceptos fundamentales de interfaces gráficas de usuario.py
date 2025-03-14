import tkinter as tk
from tkinter import messagebox

def agregar():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

def limpiar():
    lista.delete(0, tk.END)

# Crear ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("300x300")

# Etiqueta
etiqueta = tk.Label(root, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(root)
entrada.pack(pady=5)

# Botón Agregar
tagregar = tk.Button(root, text="Agregar", command=agregar)
tagregar.pack(pady=5)

# Lista
lista = tk.Listbox(root)
lista.pack(pady=5, fill=tk.BOTH, expand=True)

# Botón Limpiar
tlimpiar = tk.Button(root, text="Limpiar", command=limpiar)
tlimpiar.pack(pady=5)

# Ejecutar aplicación
root.mainloop()
