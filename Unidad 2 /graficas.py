

import tkinter as tk

# Función para agregar datos a la lista
def agregar():
    item = entrada.get()
    if item:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)  # Limpiar el campo de texto después de agregar
    else:
        print("No se ingresó ningún dato.")  # Simplemente imprimo un mensaje en la consola

# Función para limpiar los datos de la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")

# Crear los widgets
etiqueta1 = tk.Label(ventana, text="Introduce un dato:")
etiqueta1.pack(padx=20, pady=5)

entrada = tk.Entry(ventana, width=40)
entrada.pack(padx=20, pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(padx=20, pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(padx=20, pady=5)

# Crear una lista para mostrar los elementos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(padx=20, pady=10)

# Iniciar la aplicación
ventana.mainloop()
