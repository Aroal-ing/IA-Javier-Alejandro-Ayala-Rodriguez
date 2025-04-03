

Nombre: Javier Alejandro Rodriguez       Calificación:_________


1 - TIPO DE RED NEURONAL 

Teniendo en cuenta con el tipo de informacion que hemos manejado (imagenes y video) nos podemos
centrar usando una red neuronal Convolucional conciderando que los valores de entrada sean imagenes.
Al tener encuenta que la informacion requerida para identificar emociones es de tipo numerico y 
que requerimos datos en coordenadas y distancia entre puntos es mejor contar con una red neuronal
densa.

2 - PATRONES A UTILIZAR

Los patrones estaran dados por la relacion que se da entre las landmarks como por ejemplo:
distancias entre ojos, cejas, boca, pómulos, lo cuales cambian respecto a la expresión facial.

Dicho lo anterior los patrones en concreto serian lo siguientes: 

Distancias normalizadas: Estan dadas por las landmark claves.
Relaciones geometricas:  Formas entre puntos como el ancho y altura de ojos, boca, etc.
Posiciones:              Ubicación en coordenadas de puntos importantes (ojos, nariz, boca)

3 - FUNCIÓN DE ACTIVACION

Teniendo en cuenta que para procesar y clasificar los datos necesitamos aprender de relaciones
medianamente complejas lo cual se adapta perfecto a la funcionalidad que ofrece ReLU. Por otra 
parte tendremos que hacer la clasificación de emociones respecto a las salidas numericas por lo que 
usaremos Softmax unicamente para separar las emociones.

4 - NUMERO MAXIMO DE ENTRADAS

Al usar landmarks usando MediaPipe tenemos 468 landmarks de entrada.  
Teniendo en cuenta las coordenadas que vamos a usar (x,y) tenemos 468*2 entradas

Por lo tanto: 
Por cada landmark: 2 entradas (x, y).
Falta multiplicar esas entradas por el numero total de landmarks importamtes que se usaran.


5 - VALORES DE SALIDA ESPERADOS





