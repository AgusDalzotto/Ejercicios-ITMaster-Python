class Instrumento():

    def __init__(self, instrumento: int):
        self.instrumento = instrumento

    def __str__(self) -> str:
        return f"Cantidad de instrumentos en una orquesta {self.instrumento}"

    def __repr__(self) -> str:
        return f"{self.instrumento}"


class Orquesta(Instrumento):

    def __init__(self, instrumento: int):
        self.instrumento = instrumento

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
