import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        tarea = lista_tareas.get(tarea_seleccionada)
        # Agregar un cheque o marcar como completada
        tarea_completada = f"✔ {tarea}"
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, tarea_completada)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("400x400")

# Campo de entrada para la nueva tarea
entrada_tarea = tk.Entry(ventana, width=35)
entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

# Botón para agregar tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", width=20, command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=10, pady=10)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana, height=10, width=35, selectmode=tk.SINGLE)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tarea como completada
boton_completada = tk.Button(ventana, text="Marcar Completada", width=20, command=marcar_completada)
boton_completada.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Asignación de atajos de teclado
ventana.bind("<Return>", lambda event: agregar_tarea())         # Atajo para agregar tarea (Enter)
ventana.bind("<C>", lambda event: marcar_completada())          # Atajo para marcar completada (C)
ventana.bind("<Delete>", lambda event: eliminar_tarea())       # Atajo para eliminar tarea (Delete)
ventana.bind("<D>", lambda event: eliminar_tarea())             # Atajo para eliminar tarea (D)
ventana.bind("<Escape>", cerrar_aplicacion)                     # Atajo para cerrar la aplicación (Escape)

# Iniciar la aplicación
ventana.mainloop()