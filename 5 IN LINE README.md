# Cuestionario 5 en Linea - Red Neuronal 

## Ejercicio un red neuronal que pueda jugar al 5 en linea sin gravedad en un tablero de 20 * 20

** 1.- Definir el tipo de red neuronal y describir cada una de sus partes
El tipo de red neuronal segun las explicaciones de clase e investigaciones propias el tipo adecuado
seria una **red neuronal convolucional (CNN)**, debido a que son excelentes para trabajar con
con estructuras que requieran un manejo de espacio o terreno, por ejemplo tableros de juegos.
---
** 2.- Definir los patrones a utilizar
Estos patrones estarian dados por la configuracion del tablero 20x20 que representara el estado
actual de cada juego. Los patrones son los siguientes: 
 1  - Celda donde estan fichas del jugador 1.
-1  - Celda donde estan fichas del jugador 2.
 0  - Celdas vacias.
---
** 3.- Definir funcion de activación es necesaria para este problema
Conociendo a una función de activación es una función matemática que se aplica a las neuronas de una red neuronal para determinar si una neurona debe activarse o no. 
Esta función introduce no linealidad en la red, permitiéndole aprender patrones complejos.
ENTRADA
Llenado a la conclusion de que es necesaria una funcion de activacion, a manera comun la funcion **ReLU**
seria la indicada ya que evita problemas de VANISHING GRADIENTES y permite una mejor capacidad de aprendizaje. 
SALIDA
Para la capa de salida nos seria conveniente usar **SoftMax** para obtener asi cada accion posible en donde 
se podria colocar una ficha obteniendo una distribucion de probabilidades.
---
** 4.- Definir el numero máximo de entradas
Al tener un tablero de 20x20 la entradas maximas serian de 400, representando los estados
con los numeros (0, 1, -1) ya mencionados anteriormente.
---
** 5.- ¿Qué valores a la salida de la red se podrian esperar?
Si consideras la salida como las jugadas posibles, podrías esperar una matriz o vector 
con los valores correspondientes a las posiciones donde se puede colocar una ficha. 
Si usas softmax, los valores esperados serán probabilidades, es decir, un conjunto de valores entre 0 y 1.
---
** 6.- ¿Cuales son los valores máximos que puede tener el bias?
El bias en una red neuronal generalmente no tiene un valor "máximo" fijo, ya que depende del proceso de aprendizaje.
El bias se ajusta durante el entrenamiento para optimizar la salida de la red. Sin embargo, durante el proceso de entrenamiento, el valor del bias se regulariza para evitar que se vuelva demasiado grande
---
