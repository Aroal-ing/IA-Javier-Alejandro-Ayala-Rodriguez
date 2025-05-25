# -------------------------------- Generar Embeddings -------------------------------- #
import ollama
import json
import os

ruta_base = r"C:/Users/javie/OneDrive/Escritorio/Proyectos/ProyectoFinal"
embedding_path = os.path.join(ruta_base, 'embeddings.json')

# 1. Cargar embeddings actuales si existen
if os.path.exists(embedding_path):
    with open(embedding_path, 'r', encoding='utf-8') as f:
        datos_actuales = json.load(f)
else:
    datos_actuales = []

temas_existentes = [item[0] for item in datos_actuales]

# 2. Leer nuevo texto (por ejemplo, nuevas preguntas)
with open(os.path.join(ruta_base, 'temas.txt'), 'r', encoding='utf-8') as archivo:
    nuevas_lineas = [linea.strip() for linea in archivo if linea.strip() and not linea.startswith('#')]

# 3. Generar embeddings solo para nuevas preguntas
nuevos_datos = []
for pregunta in nuevas_lineas:
    if pregunta not in temas_existentes:
        response = ollama.embeddings(model='llama3', prompt=pregunta)
        nuevos_datos.append((pregunta, response['embedding']))

# 4. Guardar sin sobreescribir
datos_combinados = datos_actuales + nuevos_datos

with open(embedding_path, 'w', encoding='utf-8') as f:
    json.dump(datos_combinados, f, indent=2)


  
# -------------------------------- Generar Respuestas -------------------------------- #
  import ollama
import os

ruta_base = r'C:\Users\javie\OneDrive\Escritorio\Proyectos\ProyectoFinal'
ruta_respuestas = os.path.join(ruta_base, 'respuestas')


os.makedirs(ruta_respuestas, exist_ok=True)

# Leer las preguntas creadas en temas.txt
with open(os.path.join(ruta_base, 'temas.txt'), 'r', encoding='utf-8') as f:
    preguntas = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Generar y guardar respuestas
for i, pregunta in enumerate(preguntas):
    print(f'Generando respuesta para la pregunta {i+1}...')

    respuesta = ollama.chat(
        model='llama3',
        messages=[
            {
                'role': 'system',
                'content': 'Eres un experto en bioética con conocimientos filosóficos, médicos y tecnológicos. Responde con profundidad y claridad.'
            },
            {
                'role': 'user',
                'content': pregunta
            }
        ]
    )

    contenido = respuesta['message']['content']
    nombre_archivo = os.path.join(ruta_respuestas, f"pregunta_{i+1}.txt")

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Pregunta: {pregunta}\n\nRespuesta:\n{contenido}")

print(f"\nRespuestas generadas y guardadas en: {ruta_respuestas}")

# --------------------------------  Crear Documento   -------------------------------- #
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
import os

# Rutas
ruta_base = r'C:\Users\javie\OneDrive\Escritorio\Proyectos\ProyectoFinal'
ruta_respuestas = os.path.join(ruta_base, 'respuestas')
ruta_salida_pdf = os.path.join(ruta_base, 'Documento_Etico_Tecnologico.pdf')

# Crear PDF
doc = SimpleDocTemplate(ruta_salida_pdf, pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=72)

story = []

# Título principal
styles = getSampleStyleSheet()
titulo_style = styles['Title']
titulo = Paragraph("Proyecto Final - Reflexiones Éticas sobre el Aborto y la Eutanasia en la Era de la Inteligencia Artificial", titulo_style)
story.append(titulo)
story.append(Spacer(1, 0.3 * inch))

# Estilo para preguntas y respuestas
estilo_pregunta = ParagraphStyle(name='Pregunta', fontSize=12, leading=14, spaceAfter=6, spaceBefore=12, leftIndent=0, fontName='Helvetica-Bold')
estilo_respuesta = ParagraphStyle(name='Respuesta', fontSize=11, leading=16, spaceAfter=12, alignment=TA_JUSTIFY)

# Agregar cada pregunta y respuesta
for i in range(1, 25):  # 
    archivo = os.path.join(ruta_respuestas, f"pregunta_{i}.txt")
    if not os.path.exists(archivo):
        break

    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    if 'Respuesta:' in contenido:
        pregunta, respuesta = contenido.split('Respuesta:', 1)
    else:
        pregunta = contenido
        respuesta = ""

    story.append(Paragraph(f"Pregunta {i}:", estilo_pregunta))
    story.append(Paragraph(pregunta.strip(), estilo_respuesta))
    story.append(Paragraph(respuesta.strip(), estilo_respuesta))

# Generar el PDF
doc.build(story)

print(f"\n Documento PDF creado en: {ruta_salida_pdf}")

# --------------------------------    Fine Tuning     -------------------------------- #

import ollama
import json
import os
import math
import random

# Rutas
ruta_base = r"C:/Users/javie/OneDrive/Escritorio/Proyectos/ProyectoFinal"
ruta_embeddings = os.path.join(ruta_base, "embeddings.json")
ruta_temas = os.path.join(ruta_base, "temas.txt")

# Función para calcular similitud de coseno
def similitud_coseno(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2 + 1e-10)

# Función para generar embedding
def generar_embedding(texto):
    response = ollama.embeddings(model='llama3', prompt=texto)
    return response['embedding']

# Paso 1: Cargar embeddings existentes
if os.path.exists(ruta_embeddings):
    with open(ruta_embeddings, 'r', encoding='utf-8') as f:
        datos = json.load(f)
else:
    datos = []

temas = [item[0] for item in datos]
embeddings = [item[1] for item in datos]

# Paso 2: Pregunta del usuario
nueva_pregunta = input("Escribe una nueva pregunta ética:\n").strip()

# Paso 3: Generar embedding de la nueva pregunta
nuevo_embedding = generar_embedding(nueva_pregunta)

# Paso 4: Buscar pregunta más similar
similitudes = [similitud_coseno(nuevo_embedding, emb) for emb in embeddings]
if similitudes:
    idx_mejor = similitudes.index(max(similitudes))
    pregunta_similar = temas[idx_mejor]
else:
    pregunta_similar = "No hay preguntas previas aún."

# Paso 5: Generar respuesta
prompt = f"""
Una pregunta similar anterior fue:
"{pregunta_similar}"

Ahora responde esta pregunta nueva:
"{nueva_pregunta}"
"""

respuesta = ollama.chat(model='llama3', messages=[
    {"role": "user", "content": prompt}
])['message']['content']

print("\nRespuesta generada:\n")
print(respuesta)

# Paso 6: Guardar en temas.txt (sin duplicar)
if os.path.exists(ruta_temas):
    with open(ruta_temas, 'r', encoding='utf-8') as f:
        existentes = f.read().splitlines()
else:
    existentes = []

if nueva_pregunta not in existentes:
    with open(ruta_temas, 'a', encoding='utf-8') as f:
        f.write(nueva_pregunta + '\n\n')

# Paso 7: Guardar embedding nuevo sin duplicar
if nueva_pregunta not in temas:
    datos.append((nueva_pregunta, nuevo_embedding))
    with open(ruta_embeddings, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)

# Crear carpeta 'respuestas' si no existe
ruta_respuestas = os.path.join(ruta_base, "respuestas")
os.makedirs(ruta_respuestas, exist_ok=True)

# Generar número aleatorio único entre 50 y 150
nombre_archivo = f"pregunta_{random.randint(50, 150)}.txt"
ruta_archivo_respuesta = os.path.join(ruta_respuestas, nombre_archivo)

# Guardar pregunta y respuesta en archivo
with open(ruta_archivo_respuesta, 'w', encoding='utf-8') as f:
    f.write(f"Pregunta:\n{nueva_pregunta}\n\nRespuesta:\n{respuesta}")

    
# --------------------------------    Crear Video     -------------------------------- #

from gtts import gTTS
import fitz
import os
import subprocess

ruta_base = r'C:\Users\javie\OneDrive\Escritorio\Proyectos\ProyectoFinal'
pdf_path = os.path.join(ruta_base, 'Documento_Etico_Tecnologico.pdf')
output_audio = os.path.join(ruta_base, 'voz.mp3')
output_video = os.path.join(ruta_base, 'video_etico.mp4')
imagen_fondo = os.path.join(ruta_base, 'img.jpg')

# Extraer texto del PDF
doc = fitz.open(pdf_path)
texto = "".join(page.get_text() for page in doc)

# Generar audio con gTTS
tts = gTTS(text=texto, lang='es')
tts.save(output_audio)

# Crear video con ffmpeg usando libmp3lame 
if os.path.exists(imagen_fondo):
    cmd = [
        "ffmpeg",
        "-loop", "1",
        "-i", imagen_fondo,
        "-i", output_audio,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "libmp3lame", 
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_video
    ]
else:
    print("Imagen no encontrada. No se puede crear el video.")
    exit()

try:
    subprocess.run(cmd, check=True)
    print(f"\nVideo creado en: {output_video}")
except subprocess.CalledProcessError as e:
    print(f"\nError al crear el video: {e}")
