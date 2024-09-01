from abc import ABC, abstractmethod

class InstrumentoInterface(ABC):
    @abstractmethod
    def emitirSonido(self):
        pass
