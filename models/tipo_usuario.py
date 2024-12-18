class TipoUsuario:
    def __init__(self, id: int, tipo: str):
        self.id = id
        self.tipo = tipo

    def __repr__(self):
        return f"TipoUsuario(id={self.id}, tipo='{self.tipo}')"