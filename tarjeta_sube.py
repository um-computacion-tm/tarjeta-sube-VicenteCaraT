class NoHaySaldoException(Exception):
    pass


class UsuarioDesactivadoException(Exception):
    pass


class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = 'primario'
PRECIO_TICKET = 70
ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}

class Sube:
    def __init__(self):
        self.saldo = 0
        self.estado = "activado"
        self.grupo_beneficiario = None

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS:
            descuento = DESCUENTOS [self.grupo_beneficiario ]
            return PRECIO_TICKET - (PRECIO_TICKET * descuento /100)
        else:
            return PRECIO_TICKET

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == ACTIVADO or nuevo_estado == DESACTIVADO:
            self.estado = nuevo_estado
        else:
            raise EstadoNoExistenteException("Estado no existente")

    def pagar_pasaje(self):
        precioticket = self.obtener_precio_ticket()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado")
        if self.saldo < precioticket:
            raise NoHaySaldoException("No hay saldo suficiente")
        self.saldo -= precioticket

if __name__ == '__main__':
    pass