class Paciente():
    def __init__(self, medico: int):

        if isinstance(medico, int):
            pass

        if medico == 1:
            pass
        else:
            raise Exception("Valor invalido")

        self.medico = medico

    def __str__(self):
        return f"cantidad de medicos: {self.medico}"

    def __repr__(self):
        return f"{self.medico}"


class Medico():
    def __init__(self, paciente: int):
        self.paciente = paciente

    def __str__(self):
        return f"cantidad de medicos por paciente: {self.paciente}"

    def __repr__(self):
        return (self.paciente)
