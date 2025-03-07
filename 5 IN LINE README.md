# Cuestionario: Red Neuronal para 5 en Línea  
JAVIER ALEJANDRO AYALA RODRIGUEZ - 22120630  

Este ejercicio consiste en diseñar una red neuronal capaz de jugar al **5 en línea sin gravedad** en un tablero de **20x20**.  

## 1. Tipo de Red Neuronal  

Basado en las explicaciones de clase e investigaciones propias, el tipo de red neuronal más adecuado sería una **Red Neuronal Convolucional (CNN)**. Estas redes son ideales para manejar estructuras espaciales como tableros de juegos, ya que pueden identificar patrones en los estados del tablero.  

## 2. Patrones a Utilizar  

El estado del tablero se representa mediante una matriz **20x20**, donde cada celda puede tomar los siguientes valores:  

- `1` → Ficha del **jugador 1**  
- `-1` → Ficha del **jugador 2**  
- `0` → Celda **vacía**  

Esta representación servirá como entrada para la red neuronal.  

## 3. Función de Activación  

Las funciones de activación juegan un papel clave en las redes neuronales, ya que introducen no linealidad y permiten aprender patrones complejos.  

- **Capa Oculta**: Se utilizará **ReLU (Rectified Linear Unit)**, ya que evita el problema del *vanishing gradient* y mejora la capacidad de aprendizaje.  
- **Capa de Salida**: Se usará **Softmax**, lo que permitirá obtener una distribución de probabilidades sobre las posibles jugadas.  

## 4. Número Máximo de Entradas  

Dado que el tablero es de **20x20**, el número máximo de entradas será **400**. Cada celda del tablero se representará con los valores `{0, 1, -1}` mencionados anteriormente.  

## 5. Valores Esperados en la Salida  

Si consideramos la salida como las jugadas posibles, podemos esperar una **matriz o vector** con valores correspondientes a las posiciones donde se puede colocar una ficha.  

Si se utiliza **Softmax**, los valores de salida serán **probabilidades**, es decir, un conjunto de valores entre `0` y `1`, indicando la probabilidad de jugar en cada celda.  

## 6. Valores Máximos del Bias  

El bias en una red neuronal **no tiene un valor máximo fijo**, ya que se ajusta durante el entrenamiento para optimizar la salida de la red. Sin embargo, es común regularizarlo para evitar valores excesivamente grandes que puedan afectar el rendimiento del modelo.  

