import random
from .musico import Musico
from .instrumento import Instrumento

class Banda:
    def __init__(self, instrumentos, musicos):
        self.instrumentos = instrumentos
        self.musicos = musicos

    def llamarMusicosAleatorio(self):
        
        musicos_seleccionados = random.sample(self.musicos, len(self.instrumentos))
        instrumentos_seleccionados = random.sample(self.instrumentos, len(self.instrumentos))
        
        for musico, instrumento in zip(musicos_seleccionados, instrumentos_seleccionados):
            musico.asignarInstrumento(instrumento)
        
        return musicos_seleccionados

    def getMusicos(self):
        return self.musicos

