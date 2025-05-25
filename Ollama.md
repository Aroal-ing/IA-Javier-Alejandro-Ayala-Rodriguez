# PROYECTO 3 | OLLAMA

 Hacer un vídeo y documento utilizando modelos del lenguaje natural, utilizando por ejemplo ollama generando embeddings  y fine tuning  de los temas descritos.

 ### Pasos para la instalacion de Ollama

 **Instalamos Ollama en Windows**
![image](https://github.com/user-attachments/assets/2216cce7-5b84-4e82-963c-83b92bafaaf4)

**Instalamos LlaMa**
Ejecutamos el siguiente codigo **ollama run llama2** en terminal despues de intalar Ollama en Windows. 

**Hacemos prueba de funcionamiento**
![image](https://github.com/user-attachments/assets/cebcd17f-f04f-4e3f-b8ea-3df927043c1b)

**Se crea el entorno donde se trabajara con Python y Ollama**
![image](https://github.com/user-attachments/assets/51b07b61-1fbe-4204-acd6-dd840aea9d13)

**Creamos un txt con las preguntas de interes separadas por bloques**
![image](https://github.com/user-attachments/assets/2adce508-ec4a-4efc-b10d-e0df7da9bc4f)

**Programamos los embeddings** 
![image](https://github.com/user-attachments/assets/a2e2552b-6c0b-4dfc-bd45-d568b2a06acc)
![image](https://github.com/user-attachments/assets/b9c58281-ff7e-4355-b1c9-6966083a730f)

**Respecto a los embeddings sacamos las respuestas con el siguiente codigo y las almacenamos**
![image](https://github.com/user-attachments/assets/f863ec4e-95c7-4dbc-a01d-967aac7739d8)
![image](https://github.com/user-attachments/assets/c5416c25-68cc-4d3b-909b-eac029e40540)
![image](https://github.com/user-attachments/assets/cb88a04f-9f30-4bfc-a7eb-7b8dcfe6f1b4)
Teniendo en cuenta que mi computadora no es muy potente y Ollama require muchos recursos para procesar informacion 
solamente conteste 2 de las 19 preguntas (10 min por respuesta)

**Una ves teniendo los embeddings y unas respuestas vamos a generar el PDF** 
![image](https://github.com/user-attachments/assets/e51b9be1-3ded-490b-ae1f-226d8636c39c)
![image](https://github.com/user-attachments/assets/8ac2b1c0-2055-4945-b058-e81c6a267532)

**Teniendo terminado lo mas importante vamos a empezar con la implementación de fine-tuning**
Con la informacion que tenemos hasta el momento podemos hacer un psudo fine-tuning...

![image](https://github.com/user-attachments/assets/5d6b24b2-422f-4357-87ea-5d280cc49931)

Al ejecutar el script este usa la informacón de los embeddings generados anteriormente con el proposito 
de buscar la pregunta mas parecida a la nueva pregunta y respecto a eso dar una respuesta.

![image](https://github.com/user-attachments/assets/b03ceb99-7f14-488a-a9c4-45f952f1156f)

**Como paso final vamos a ajustar el pseudo fine-tuning para que aprenda de el mismo y agregue lo aprendido a los embeddings para su uso posterior** 

![image](https://github.com/user-attachments/assets/d9920436-779a-4de2-a656-0aba46d0f7e5)

El codigo permite diferentes cosas, al hacer una nueva pregunta se guarda en el .txt a partir de aqui se generan nuevos embeddings 
para las respuestas las cuales se agregaran al PDF. 

![image](https://github.com/user-attachments/assets/cfe785c7-1618-4a57-819b-5042a6ed0672)
![image](https://github.com/user-attachments/assets/57dcebe7-f33c-4fb9-a29a-6954e22e782e)

**Finalmente vamos a crear el video usando la libreria ffmpeg moviepy PyMuPDF**
![image](https://github.com/user-attachments/assets/a07aabec-bd1d-4dcc-b273-5ec9e741e2e8)
![image](https://github.com/user-attachments/assets/8e0289fa-7210-4d5a-9871-b2e693889317)

















