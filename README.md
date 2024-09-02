# Chisga Musical - Modelos de Programación II

Universidad Distrital Francisco José de Caldas  
Proyecto Curricular de Ingeniería de Sistemas

**Asignatura:** Modelos de Programación II  
**Profesor:** Alejandro Paolo Daza Corredor

---

## Integrantes

- Amir Zoleyt Vanegas Cárdenas - 20211020015 <br> azvanegasc@udistrital.edu.co
- Esteban Alejandro Villalba Delgadillo - 20212020064 <br> eavillalbad@udistrital.edu.co
- Samuel Antonio Sanchez Peña - 20212020151 <br> samasanchezp@udistrital.edu.co

---

## Descripción del Proyecto

Este proyecto consiste en la creación de una banda musical para asistir a una chisga, formada por un número aleatorio de músicos y una colección de instrumentos variados, como guitarras, violines, pianos, entre otros. Cada vez que se llame a una banda, el número de músicos siempre será distinto y tendrá cada uno un instrumento asignado aleatoriamente, el cual afinarán y tocarán.

### Objetivos

- Simular la interacción entre los músicos y los instrumentos buscando generar una banda musical aleatoria en cada ejecución, donde dicha banda afine y toque los instrumentos en la chizga musical.

- Dominar los conceptos relacionados al análisis, diseño y programación en el paradigma orientado a objetos a través de la realización de este programa.

## Características del proyecto

La aplicación hace uso de las siguientes bibliotecas para su debido funcionamiento:

- Random: Generación de números aleatorios para devolver siempre una banda musical de un tamaño n cada ejecución.

- ABC: Abstract Base Classes, biblioteca para la construcción de software orientado a objetos con características como clases abstractas o interfaces. Es de utilidad para la representación adecuada del diseño.

Es importante notar que la biblioteca ABC obliga a la creación de una carpeta de las intefaces para la construcción del programa. Así mismo, por la naturaleza de Python se llaman a los métodos __new__() e __init__() para la instanciación del objeto con sus atributos.

Las características de diseño del programa se encuentran en la carpeta diagramas. A continuación, se muestran los diagramas UML correspondientes al diseño.

### Diagrama de Clases

El siguiente diagrama de clases muestra la estructura de las clases utilizadas en el proyecto, destacando las relaciones entre clases de los paquetes `banda`, `instrumento`, e `interfaces`. Este diagrama proporciona una visión general de cómo se organizan las entidades principales y cómo interactúan entre sí dentro del sistema.

![Diagrama de Clases](https://github.com/Inaryuta/Entregable-I-Modelos-Programacion-II/blob/master/diagramas/imagenes/Diagrama%20de%20Clases.png)

###  Diagrama de Secuencia

A continuación, se presenta el diagrama de secuencia que ilustra el flujo principal de ejecución del programa, desde la inicialización de los objetos `Musicos` y las implementaciones de la interfaz `Instrumento`, terminando en la asignación de instrumentos y la ejecución de la banda formada aleatoriamente para la chisga musical.

![Diagrama de Secuencia](https://github.com/Inaryuta/Entregable-I-Modelos-Programacion-II/blob/master/diagramas/imagenes/Diagrama%20de%20Secuencia.png)

### Instrucciones de ejecución

Para ejecutar el proyecto, primero debe verificar que tenga instalando Python en su sistema Operativo; preferiblemente una versión 3.10 o mayor.

Estas son las siguientes instrucciones para ejecutar el proyecto:

1. **Clonar el repositorio:**
```bash
   git clone https://github.com/Inaryuta/Modelos-II.git
```

2. **Navega al directorio del repositorio clonado:**
```bash
   cd Modelos-II
```

3. **Ejecutar el main:**
```bash
   python main.py
```

---