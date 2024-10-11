class Usuario:
    def __init__(self, nombre, id_usuario, correo_electronico):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo_electronico = correo_electronico

    def registrar_usuario(self):
        print(f"Usuario registrado: {self.nombre}")

    def consultar_libros(self):
        print(f"{self.nombre} está consultando los libros.")
