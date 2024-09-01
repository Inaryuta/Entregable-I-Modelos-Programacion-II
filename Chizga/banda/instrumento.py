from interfaces.instrumento_interface import InstrumentoInterface

class Instrumento(InstrumentoInterface):
    def emitirSonido(self):
        pass

class Guitarra(Instrumento):
    def emitirSonido(self):
        print("Guitarra suena.")

class Trompeta(Instrumento):
    def emitirSonido(self):
        print("Trompeta suena.")

class Violin(Instrumento):
    def emitirSonido(self):
        print("Violín suena.")

class Piano(Instrumento):
    def emitirSonido(self):
        print("Piano suena.")


class Saxofon(Instrumento):
    def emitirSonido(self):
        print("Saxofón suena.")

class Bajo(Instrumento):
    def emitirSonido(self):
        print("Bajo suena.")

class Xilofono(Instrumento):
    def emitirSonido(self):
        print("Xilófono suena.")

class Flauta(Instrumento):
    def emitirSonido(self):
        print("Flauta suena.")

class Bateria(Instrumento):
    def emitirSonido(self):
        print("Batería suena.")

class Acordeon(Instrumento):
    def emitirSonido(self):
        print("Acordeón suena.")
