class MovimientoCuenta:
    def __init__(self, id: int, cuenta: int, tipo_movimiento: str, monto: float):
        self.id = id
        self.cuenta = cuenta
        self.tipo_movimiento = tipo_movimiento  # This should match the keyword argument
        self.monto = monto

    def __repr__(self):
        return (f"MovimientoCuenta(id={self.id}, cuenta={self.cuenta}, "
                f"tipo_movimiento='{self.tipo_movimiento}', monto={self.monto})")