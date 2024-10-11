class biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.obtener_titulo()}")

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_informacion()
