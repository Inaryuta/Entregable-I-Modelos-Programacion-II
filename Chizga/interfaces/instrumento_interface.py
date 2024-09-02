from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def emitirSonido(self):
        pass

    @abstractmethod
    def ajustarFrecuencias(self):
        pass
