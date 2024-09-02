import random
from .musico import Musico
from interfaces.instrumento_interface import Instrumento

class Banda:
    def __init__(self, instrumentos: Instrumento, musicos: Musico):
        self.instrumentos = instrumentos
        self.musicos = musicos

    def llamarMusicosAleatorio(self):
        cantidad_aleatoria = random.randint(1, len(self.musicos))

        musicos_seleccionados = random.sample(self.musicos, cantidad_aleatoria)
        instrumentos_seleccionados = random.sample(self.instrumentos, cantidad_aleatoria)
        
        for musico, instrumento in zip(musicos_seleccionados, instrumentos_seleccionados):
            musico.setInstrumento(instrumento)
        
        return musicos_seleccionados

    def getMusicos(self):
        return self.musicos

