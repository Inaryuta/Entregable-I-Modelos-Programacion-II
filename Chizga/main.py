from banda import Guitarra, Trompeta, Violin, Piano, Saxofon, Bajo, Xilofono, Flauta, Bateria, Acordeon, Musico, Banda

def main():
    instrumentos = [
        Guitarra(),
        Trompeta(),
        Violin(),
        Piano(),
        Saxofon(),
        Bajo(),
        Xilofono(),
        Flauta(),
        Bateria(),
        Acordeon()
    ]
    
    musicos = [
        Musico("Samuel"),
        Musico("Esteban"),
        Musico("Dilan"),
        Musico("Alejandro"),
        Musico("Camilo"),
        Musico("Adrián"),
        Musico("Jesús"),
        Musico("Mariana"),
        Musico("Sara"),
        Musico("Amir")
    ]

    banda = Banda(instrumentos, musicos)
    banda_preparada = banda.llamarMusicosAleatorio()

    for musico in banda_preparada:
        musico.afinar()
        musico.tocar()
        print("") #Espaciado al imprimir en interfaz

if __name__ == "__main__":
    main()
