import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para mostrar los eventos
        self.frame_list = ttk.Frame(self.root)
        self.frame_list.pack(pady=10)

        # Titulo de la agenda
        self.title_label = ttk.Label(self.frame_list, text="Eventos Programados", font=("Arial", 16))
        self.title_label.pack()

        # Crear el Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10)

        # Frame para el formulario de entrada
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=10)

        # Etiquetas y campos de entrada
        self.create_input_fields()

        # Botones de acción
        self.create_action_buttons()

    def create_input_fields(self):
        """Crea las etiquetas y los campos de entrada para el formulario"""
        self.date_label = ttk.Label(self.frame_input, text="Fecha:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = ttk.Label(self.frame_input, text="Hora:")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.frame_input)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        self.desc_label = ttk.Label(self.frame_input, text="Descripción:")
        self.desc_label.grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.frame_input)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

    def create_action_buttons(self):
        """Crea los botones para agregar, eliminar y salir"""
        self.add_button = ttk.Button(self.frame_input, text="Agregar Evento", command=self.agregar_evento)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = ttk.Button(self.frame_input, text="Eliminar Evento Seleccionado",
                                        command=self.eliminar_evento)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.exit_button = ttk.Button(self.frame_input, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=5, column=0, columnspan=2, pady=5)

    def agregar_evento(self):
        """Agrega un evento a la lista de eventos"""
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        # Validar los campos de entrada
        if not self.validar_campos(fecha, hora, descripcion):
            return

        # Insertar el evento en el Treeview
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada
        self.limpiar_campos()

    def validar_campos(self, fecha, hora, descripcion):
        """Valida que los campos no estén vacíos"""
        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return False
        return True

    def limpiar_campos(self):
        """Limpia los campos de entrada"""
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina un evento seleccionado de la lista"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")
            return

        # Confirmación de eliminación
        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)


# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()