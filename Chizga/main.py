from banda import Guitarra, Trompeta, Violin, Piano, Saxofon, Bajo, Xilofono, Flauta, Bateria, Acordeon, Musico, Banda

def main():
    # Instancia de instrumentos
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
    
    # Instancia de músicos
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

    # Crear la banda y asignar instrumentos a los músicos aleatoriamente
    banda = Banda(instrumentos, musicos)
    banda_preparada = banda.llamarMusicosAleatorio()

    # Hacer que los músicos seleccionados toquen sus instrumentos
    for musico in banda_preparada:
        musico.afinar()
        musico.tocar()

if __name__ == "__main__":
    main()
