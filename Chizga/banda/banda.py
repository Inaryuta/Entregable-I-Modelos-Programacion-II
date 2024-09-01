from .musico import Musico
from .instrumento import Instrumento

class Banda:
    def __init__(self, instrumentos, musicos):
        self.instrumentos = instrumentos
        self.musicos = musicos

    def llamarMusicosAleatorio(self):
        for musico, instrumento in zip(self.musicos, self.instrumentos):
            musico.asignarInstrumento(instrumento)
        return self

    def getMusicos(self):
        return self.musicos
