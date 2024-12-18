class Cuenta:
    def __init__(self, id: int, usuario: int, tipo: int, saldo: float):
        self.id = id
        self.usuario = usuario
        self.tipo = tipo
        self.saldo = saldo

    def __repr__(self):
        return (f"Cuenta(id={self.id}, usuario={self.usuario}, tipo={self.tipo}, "
                f"saldo={self.saldo})")