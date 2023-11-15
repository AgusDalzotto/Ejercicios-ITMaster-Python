class Avion():

    def __init__(self, avion: int, aviones_estacionados: int):
        self.avion = avion
        self.aviones_estacionados = aviones_estacionados

    def __str__(self):
        return f"Cantidad de aviones en un aeropuerto {self.avion}, cantidad de aviones estacionados: {self.aviones_estacionados}"

    def __repr__(self):
        return f"{self.avion}, {self.aviones_estacionados}"


class Aeropuerto(Avion):

    def __init__(self):
        super.__init__()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()
