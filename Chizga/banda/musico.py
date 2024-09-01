from .instrumento import Instrumento

class Musico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumento = None

    def asignarInstrumento(self, instrumento: Instrumento):
        self.instrumento = instrumento

    def tocar(self):
        if self.instrumento:
            print(f"{self.nombre} está tocando su {self.instrumento.__class__.__name__}.")
            self.instrumento.emitirSonido()
        else:
            print(f"{self.nombre} no tiene un instrumento asignado.")
