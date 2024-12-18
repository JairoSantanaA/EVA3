class Usuario:
    def __init__(self, id: int, rut: str, nombre: str, apellido: str, correo: str, usuario: str, clave: str, tipo: int):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.usuario = usuario
        self.clave = clave
        self.tipo = tipo

    def __repr__(self):
        return (f"Usuario(id={self.id}, rut='{self.rut}', nombre='{self.nombre}', "
                f"apellido='{self.apellido}', correo='{self.correo}', "
                f"usuario='{self.usuario}', tipo={self.tipo})")