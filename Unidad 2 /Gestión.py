import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task():
    task = entry.get()  # Obtener el texto del campo de entrada
    if task != "":
        listbox.insert(tk.END, task)  # Añadir la tarea a la lista
        entry.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)  # Eliminar la tarea
        listbox.insert(selected_task_index, task + " (Completada)")  # Volver a insertarla con "(Completada)"
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

# Función para cerrar la aplicación con la tecla Escape
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear el campo de entrada para nuevas tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Crear los botones de la interfaz
add_button = tk.Button(root, text="Añadir tarea", command=add_task)
add_button.pack(pady=5)

mark_button = tk.Button(root, text="Marcar como completada", command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
delete_button.pack(pady=5)

# Crear la lista de tareas
listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Asignar atajos de teclado
root.bind('<Return>', lambda event: add_task())  # Tecla Enter para añadir tarea
root.bind('<c>', lambda event: mark_completed())  # Tecla "C" para marcar como completada
root.bind('<Delete>', lambda event: delete_task())  # Tecla "Delete" para eliminar tarea
root.bind('<Escape>', close_app)  # Tecla Escape para cerrar la aplicación

# Ejecutar la aplicación
root.mainloop()
