
class Estante():

    def __init__(self, estantes):
        self. estantes = estantes

    def __str__(self):
        return f"Cantidad de estantes de una biblioteca {self.estantes}"

    def __repr__(self):
        return f"{self.estantes}"


class Biblioteca(Estante):
    def __init__(self, estantes: int):
        self.estantes = estantes

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()
