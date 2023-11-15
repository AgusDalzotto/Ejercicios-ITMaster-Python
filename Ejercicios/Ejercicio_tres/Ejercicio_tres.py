class Empresa():
    def __init__(self, empleados: int):
        if isinstance(empleados, int):
            self.empleados = empleados
        else:
            raise Exception("Valor invalido")

    def __str__(self) -> str:
        return f"La cantidad de empleados de la empresa es: {self.empleados}"

    def __repr__(self) -> str:
        return f"{self.empleados}"


class Empleado():

    def __init__(self, empresa: int):
        if isinstance(empresa, int):
            pass
        else:
            raise Exception("Valor invalido")

        if empresa == 1:
            pass
        else:
            raise Exception("Valor invalido")

        self.empresa = empresa

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass
