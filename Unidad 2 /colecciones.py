
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', '{self.categoria}', '{self.isbn}')"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []
    
    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)
    
    def eliminar_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()
    
    def anadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido.")
    
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")
    
    def registrar_usuario(self, usuario):
        self.usuarios.add(usuario)
        print(f"Usuario '{usuario.nombre}' registrado.")
    
    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
            if usuario:
                usuario.agregar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print("Usuario no encontrado.")
        else:
            print("Libro no disponible.")
    
    def devolver_libro(self, isbn, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            usuario.eliminar_libro(isbn)
            print(f"Libro con ISBN {isbn} devuelto.")
        else:
            print("Usuario no encontrado.")
    
    def buscar_libro(self, criterio):
        return [libro for libro in self.libros.values() if criterio.lower() in libro.titulo.lower()]
    
    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            return usuario.libros_prestados
        return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell", "Distopía", "11111")
libro2 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", "Novela", "22222")

# Crear usuarios
usuario1 = Usuario("Carlos Martínez", 3)
usuario2 = Usuario("Ana Rodríguez", 4)

# Registrar usuarios y añadir libros
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

# Prestar libros
biblioteca.prestar_libro("11111", 3)

# Buscar libro
libros_encontrados = biblioteca.buscar_libro("1984")
print("Libros encontrados:", libros_encontrados)

# Devolver libro
biblioteca.devolver_libro("11111", 3)
