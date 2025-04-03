# **Nombre:** Javier Alejandro Rodriguez  
**Calificación:** _________  

---

## TIPO DE RED NEURONAL  
Teniendo en cuenta el tipo de información manejada (imágenes y video), podemos centrarnos en el uso de una **Red Neuronal Convolucional (CNN)**, considerando que los valores de entrada son imágenes.  

Sin embargo, dado que la información requerida para identificar emociones es **numérica** y depende de coordenadas y distancias entre puntos, es mejor emplear una **Red Neuronal Densa (DNN)**.

---

## PATRONES A UTILIZAR  
Los patrones estarán definidos por la relación entre las **landmarks**, como:  

- **Distancias normalizadas** → Basadas en landmarks clave.  
- **Relaciones geométricas** → Formas entre puntos (ancho/altura de ojos, boca, etc.).  
- **Posiciones** → Ubicación en coordenadas de puntos importantes (ojos, nariz, boca).  

---

## FUNCIÓN DE ACTIVACIÓN  
Para procesar y clasificar los datos, necesitamos aprender relaciones **complejas**:  

- Utilizaremos **ReLU** para las capas ocultas, ya que es eficiente en aprendizaje profundo.  
- Para la **clasificación de emociones**, emplearemos **Softmax**, que nos permitirá obtener probabilidades asociadas a cada emoción.  

---

## NÚMERO MÁXIMO DE ENTRADAS  
Al usar **MediaPipe**, contamos con **468 landmarks de entrada**.  

Dado que utilizamos las coordenadas **(x, y)** de cada landmark:  
\[
\text{Entradas totales} = 468 \times 2 = 936
\]

**Nota:** Este número puede variar según los landmarks seleccionados como relevantes.  

---

## VALORES DE SALIDA ESPERADOS  
Para la clasificación de emociones, podemos definir categorías como:  

["Feliz", "Triste", "Enojado", "Neutral"]

con probabilidades como las siguientes : 

[0.88, 0.02, 0.07, 0.03] indicando que esta un 88% FELIZ.




## VALORES MAXIMOS PARA BIAS 

Teniendo en cuenta la definición de BIAS en las redes neuronales, no hay un limite que
se vaya a necesitar dado que el BIAS se ajusta durante el proceso de entrenamiento pero 
generalmente siempre se usa inicialmente con valores pequeños.







