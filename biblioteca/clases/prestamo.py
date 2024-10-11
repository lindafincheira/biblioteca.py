class Prestamo:
    def __init__(self, fecha_inicio, fecha_fin, estado):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def realizar_prestamo(self):
        print(f"Préstamo realizado. Estado: {self.estado}")

    def finalizar_prestamo(self):
        print("Préstamo finalizado.")

    def consultar_estado(self):
        print(f"El estado del préstamo es: {self.estado}")
