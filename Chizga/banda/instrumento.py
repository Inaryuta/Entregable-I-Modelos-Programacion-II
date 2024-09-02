from interfaces.instrumento_interface import Instrumento

class Guitarra(Instrumento):
    def emitirSonido(self):
        print("Guitarra suena.")
    
    def ajustarFrecuencias(self):
        print("""Frecuencias de cuerdas de guitarra 
              ajustadas a 2.41 Hz, 110 Hz, 146.83 Hz, 196.00 Hz, 
              246.94 Hz y 329.63 Hz""")


class Trompeta(Instrumento):
    def emitirSonido(self):
        print("Trompeta suena.")
    
    def ajustarFrecuencias(self):
        print("Frecuencia de trompeta ajustada a 440 Hz")


class Violin(Instrumento):
    def emitirSonido(self):
        print("Violín suena.")
    
    def ajustarFrecuencias(self):
        print("""Frecuencia de cuerdas de violín 
              ajustadas a 196 Hz, 293.66 Hz, 440 Hz, 
              y 659.26 Hz""")


class Piano(Instrumento):
    def emitirSonido(self):
        print("Piano suena.")

    def ajustarFrecuencias(self):
        print("Frecuencia de piano ajustada a 440Hz")


class Saxofon(Instrumento):
    def emitirSonido(self):
        print("Saxofón suena.")
    
    def ajustarFrecuencias(self):
        print("Frecuencia de saxofón ajustada a 440 Hz")


class Bajo(Instrumento):
    def emitirSonido(self):
        print("Bajo suena.")
    
    def ajustarFrecuencias(self):
        print("""Frecuencia de cuerdas de bajo 
              ajustadas a 41.20 Hz, 55.00 Hz, 73.42 Hz, 
              y 98.00 Hz""")


class Xilofono(Instrumento):
    def emitirSonido(self):
        print("Xilófono suena.")
    
    def ajustarFrecuencias(self):
        print("Frecuencia de xilófono ajustada a 440 Hz")


class Flauta(Instrumento):
    def emitirSonido(self):
        print("Flauta suena.")
    
    def ajustarFrecuencias(self):
        print("Frecuencia de flauta ajustada a 440 Hz")


class Bateria(Instrumento):
    def emitirSonido(self):
        print("Batería suena.")

    def ajustarFrecuencias(self):
        print("Caja de la batería afinada a 155Hz")
        print("Tom-Toms afinados a 220 Hz")
        print("Bombos afinandos a 41.20 Hz")

class Acordeon(Instrumento):
    def emitirSonido(self):
        print("Acordeón suena.")
    
    def ajustarFrecuencias(self):
        print("Frecuencia de acordeon ajustada a 440 Hz")
