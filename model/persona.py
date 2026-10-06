class Persona:
    def __init__(self, rut, nombre, apellido):
        # CAMBIO 3: antes era "self.__rut = rut" (sin revisar nada).
        # Ahora pasa por el setter, que valida el RUT.
        self.rut = rut
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def rut(self):
        return self.__rut

    # CAMBIO 3: setter nuevo. Lanza ValueError si el RUT no es valido.
    @rut.setter
    def rut(self, valor):
        if not Persona._rut_es_valido(valor):
            raise ValueError(f"RUT inválido: {valor!r}")
        self.__rut = valor

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    # CAMBIO 3: metodo nuevo. Calcula el digito verificador (modulo 11).
    @staticmethod
    def _rut_es_valido(rut):
        if not isinstance(rut, str):
            return False
        limpio = rut.replace(".", "").replace(" ", "").upper()
        if "-" not in limpio:
            return False
        cuerpo, _, dv = limpio.partition("-")
        if not cuerpo.isdigit() or len(dv) != 1:
            return False
        suma = 0
        for i, digito in enumerate(reversed(cuerpo)):
            suma += int(digito) * (2 + i % 6)
        resto = 11 - suma % 11
        esperado = "0" if resto == 11 else "K" if resto == 10 else str(resto)
        return dv == esperado

    def validar_rut(self):
        # CAMBIO 3: antes solo miraba que el texto tuviera 3 o mas caracteres.
        return Persona._rut_es_valido(self.__rut)
