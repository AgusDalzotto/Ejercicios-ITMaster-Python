class Avion():

    def __init__(self, avion: int, aviones_estacionados: int):
        self.avion = avion
        self.aviones_estacionados = aviones_estacionados

    def __str__(self):
        return f"Cantidad de aviones en un aeropuerto {self.avion}, cantidad de aviones estacionados: {self.aviones_estacionados}"

    def __repr__(self):
        return f"{self.avion}, {self.aviones_estacionados}"


class Aeropuerto():

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
