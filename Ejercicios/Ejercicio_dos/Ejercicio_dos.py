class Libro():
    def __init__(self, escritor: int):

        if escritor == 1:
            pass
        else:
            raise Exception("Valor invalido")

        self.escritor = escritor

    def __str__(self):
        return f"Libro escrito por: {self.escritor} autor/res"

    def __repr__(self):
        return f"{self.escritor}"


class Escritor():
    def __init__(self, libros: int):
        self.libros = libros

    def __str__(self):
        return f"cantidad de libros escritos por un mismo autor: {self.libros}"

    def __repr__(self):
        return f"{self.libros}"
