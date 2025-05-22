import pygame
import heapq

# Inicializar pygame y pygame.font para usar las fuentes
pygame.init()
pygame.font.init()


# Configuración de la ventana del juego y el tamaño de la cuadrícula
ANCHO_VENTANA = 600  
FILAS = 10  
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA + 100))  
pygame.display.set_caption("Visualización de A*")  


# Definición de los colores (RGB)
BLANCO = (23, 32, 42)  
NEGRO = (255,255,255)  
GRIS = (128, 128, 128)  
VERDE = (0, 255, 0)  
ROJO = (255, 0, 0)  
NARANJA = (118, 215, 196)  
PURPURA = (128, 0, 128)  
AZUL = (0, 0, 255)  

# Definición de los costos de movimiento
COSTO_HORIZONTAL_VERTICAL = 10 
COSTO_DIAGONAL = 14  

# Clase Nodo que representa cada celda en la cuadrícula
class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila  
        self.col = col  
        self.x = fila * ancho  #x
        self.y = col * ancho   #y
        self.color = BLANCO  
        self.ancho = ancho  
        self.total_filas = total_filas  # Total de filas en la cuadrícula
        self.g = float("inf")           # Costo desde el nodo inicial (inicialmente infinito)
        self.h = 0                      # Heurística (distancia estimada al nodo final)
        self.f = float("inf")           # Valor de la función f = g + h
        self.padre = None               # Nodo padre (para reconstruir el camino)
        
        self.numero = col * total_filas + fila + 1

    # Método para comparar nodos por el valor de la función f
    def __lt__(self, otro):
        return self.f < otro.f

    def get_pos(self):
        return self.fila, self.col  

    def es_pared(self):
        return self.color == NEGRO    # Distinguir Pared

    def es_inicio(self):
        return self.color == NARANJA  # Distinguir Inicio

    def es_fin(self):
        return self.color == PURPURA  # Distinguir Fin



    # Métodos para definir INICIO, FIN Y PAREDES
    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = PURPURA

    def hacer_camino(self):
        if not self.es_inicio() and not self.es_fin():
            self.color = AZUL  # Si el nodo no es ni inicio ni fin, es parte del camino


    # Método para dibujar el nodo en la pantalla
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))
        font = pygame.font.Font(None, 20)  
        text = font.render(str(self.numero), True, NEGRO)  
        ventana.blit(text, (self.x + 5, self.y + 20))  



# Función para crear la cuadrícula de nodos
def crear_grid(filas, ancho):
    grid = []
    ancho_nodo = ancho // filas  # Calcular el tamaño de cada nodo
    for i in range(filas):
        grid.append([])
        for j in range(filas):
            nodo = Nodo(i, j, ancho_nodo, filas)  # Crear cada nodo
            grid[i].append(nodo)
    return grid


# Función de heurística - Distancia de Manhattan para A*
def heuristica(nodo1, nodo2):
    x1, y1 = nodo1.get_pos()
    x2, y2 = nodo2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2)  # Calcula la distancia de Manhattan


# Función para reconstruir el camino desde el nodo final
def reconstruir_camino(nodo_actual):
    camino = []
    while nodo_actual.padre:
        camino.append(nodo_actual.numero)  
        nodo_actual.hacer_camino()         # Marcar el nodo como parte del camino
        nodo_actual = nodo_actual.padre    # Ir al nodo padre
    return camino[::-1]                    # Retornar el camino en orden inverso, es decir de inicio a fin 


# Función para obtener los vecinos de un nodo (incluyendo diagonales)
def obtener_vecinos(nodo, grid):
    vecinos = []
    filas = len(grid)
    # Direcciones (arriba, abajo, izquierda, derecha, diagonales)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d in direcciones:
        fila, col = nodo.fila + d[0], nodo.col + d[1]
        # Cuidar que el vecino esté dentro de los límites de la cuadrícula
        if 0 <= fila < filas and 0 <= col < filas:
            vecino = grid[fila][col]
            if not vecino.es_pared():  
                # Agregar el vecino y el costo correspondiente (diagonal o recto)
                vecinos.append((vecino, COSTO_DIAGONAL if d[0] != 0 and d[1] != 0 else COSTO_HORIZONTAL_VERTICAL))
    return vecinos


# Función principal de A* para encontrar el camino más corto
def algoritmo_a_estrella(grid, inicio, fin):
    inicio.g = 0
    inicio.h = heuristica(inicio, fin)
    inicio.f = inicio.h
    open_set = [(inicio.f, inicio)]  # Conjunto abierto de nodos a explorar (con prioridad)
    heapq.heapify(open_set)          # Prioriza el nodo con el menor valor
    
    while open_set:
        _, nodo_actual = heapq.heappop(open_set)  # Obtener el nodo con menor f
        
        if nodo_actual == fin:
            camino = reconstruir_camino(fin)  # Si se llegó al nodo final, reconstruir el camino
            print("Ruta más corta:", camino)
            return True
        
        # Explorar los vecinos del nodo actual
        for vecino, costo in obtener_vecinos(nodo_actual, grid):
            nuevo_g = nodo_actual.g + costo
            if nuevo_g < vecino.g:                  # Si el nuevo costo g es menor que el anterior
                vecino.g = nuevo_g
                vecino.h = heuristica(vecino, fin)
                vecino.f = vecino.g + vecino.h      # Actualizar el valor de f
                vecino.padre = nodo_actual          # Establecer el nodo actual como el padre del vecino
                heapq.heappush(open_set, (vecino.f, vecino))  # Añadir el vecino al conjunto abierto
    
    return False                                              # Si no se encuentra un camino


# Función para obtener la posición de la celda al hacer clic
def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

# Función para dibujar la cuadrícula y los nodos
def dibujar(ventana, grid, filas, ancho):
    ventana.fill(BLANCO) 
    for fila in grid:
        for nodo in fila:
            nodo.dibujar(ventana)  
    pygame.display.update()  

# Función principal que ejecuta el juego
def main():
    grid = crear_grid(FILAS, ANCHO_VENTANA)  
    inicio = None  
    fin = None  
    # Rectángulos para los botones de "Buscar" y "Salir"
    boton_buscar_rect = pygame.Rect(ANCHO_VENTANA // 2 - 50, ANCHO_VENTANA + 10, 100, 30)
    boton_salir_rect = pygame.Rect(ANCHO_VENTANA // 2 - 50, ANCHO_VENTANA + 50, 100, 30)
    corriendo = True  # Variable para controlar el bucle del juego

    while corriendo:
        dibujar(VENTANA, grid, FILAS, ANCHO_VENTANA)  # Dibujar la cuadrícula y los nodos
        
        # Botón de "Buscar"
        pygame.draw.rect(VENTANA, VERDE, boton_buscar_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Buscar", True, NEGRO)
        VENTANA.blit(text, (ANCHO_VENTANA // 2 - 25, ANCHO_VENTANA + 15))
        
        # Botón de "Salir"
        pygame.draw.rect(VENTANA, ROJO, boton_salir_rect)
        text = font.render("Salir", True, NEGRO)
        VENTANA.blit(text, (ANCHO_VENTANA // 2 - 25, ANCHO_VENTANA + 55))

        pygame.display.update()
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Si el usuario cierra la ventana
                corriendo = False
            
            if pygame.mouse.get_pressed()[0]:   # Si el usuario hace clic
                pos = pygame.mouse.get_pos()    # Obtener la posición del clic
                
                # Acción del botón "Buscar"
                if boton_buscar_rect.collidepoint(pos) and inicio and fin:
                         encontrado = algoritmo_a_estrella(grid, inicio, fin)  # Llamar una sola vez y almacenar el resultado
                         dibujar(VENTANA, grid, FILAS, ANCHO_VENTANA)  # Redibujar la pantalla con el camino resaltado 

                         if encontrado:
                             pygame.time.delay(5000)
                             return
                         
                         if not encontrado:  # Si no se encontró un camino, mostrar un mensaje
                              font = pygame.font.Font(None, 36)
                              mensaje = font.render("No hay camino posible", True, ROJO)
                              VENTANA.blit(mensaje, (ANCHO_VENTANA // 2 - 100, ANCHO_VENTANA // 2))
                              pygame.display.update()
                              pygame.time.delay(2000)
                              corriendo = False  # Salir del juego

                
                # Acción del botón "Salir"
                elif boton_salir_rect.collidepoint(pos):
                    corriendo = False  # Salir del juego
                
                # Selección de nodos
                else:
                    fila, col = obtener_click_pos(pos, FILAS, ANCHO_VENTANA)
                    nodo = grid[fila][col]
                    if not inicio and nodo != fin:
                        inicio = nodo
                        inicio.hacer_inicio()  # Marcar como nodo de inicio
                    elif not fin and nodo != inicio:
                        fin = nodo
                        fin.hacer_fin()  # Marcar como nodo de fin
                    elif nodo != fin and nodo != inicio:
                        nodo.hacer_pared()  # Marcar como nodo de pared
    
    pygame.quit()  # Salir de pygame

# Ejecutar el juego
main()
