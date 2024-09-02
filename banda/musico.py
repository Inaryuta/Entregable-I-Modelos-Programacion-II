import time
from interfaces.instrumento_interface import Instrumento

class Musico:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.instrumento = None

    def setInstrumento(self, instrumento: Instrumento):
        self.instrumento = instrumento


    def tocar(self):
        if self.instrumento:
            print(f"{self.nombre} está tocando su {self.instrumento.__class__.__name__}.")
            time.sleep(0.25)
            self.instrumento.emitirSonido()
        else:
            print(f"{self.nombre} no tiene un instrumento asignado.")
    

    def afinar(self):
        if self.instrumento:
            print(f"{self.nombre} está afinando su {self.instrumento.__class__.__name__}.")
            time.sleep(1)
            self.instrumento.ajustarFrecuencias()
        else:
            print(f"{self.nombre} no tiene un instrumento asignado.")
