import pygame
import os

pygame.init()

ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 900
TAMANIO_TILE = 30
TAMANIO_TILE_JUGADOR = 30
TILES_HORIZONTAL = ANCHO_PANTALLA // TAMANIO_TILE  # 20 tiles
TILES_VERTICAL = ALTO_PANTALLA // TAMANIO_TILE  # 15 tiles

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Juego de Plataforma con Colisiones Detalladas')

BLANCO = (255, 255, 255)
FONDO = pygame.image.load('assets/tiles/fondo.png').convert()
FONDO = pygame.transform.scale(FONDO, (ANCHO_PANTALLA, ALTO_PANTALLA))

VELOCIDAD_JUGADOR = 6
GRAVEDAD = 1
FUERZA_SALTO = -10
SUPER_SALTO_MULTIPLIER = -3  # Multiplier for super jump

def cargar_sprites(ruta, cantidad):
    imagenes = []
    for i in range(cantidad):
        imagen = pygame.image.load(os.path.join(ruta, f'{i}.png')).convert_alpha()
        imagen = pygame.transform.scale(imagen, (TAMANIO_TILE_JUGADOR, TAMANIO_TILE_JUGADOR))
        imagenes.append(imagen)
    return imagenes

sprites_parado = cargar_sprites('assets/jugador/parado', 1)
sprites_izquierda = cargar_sprites('assets/jugador/izquierda', 8)
sprites_derecha = cargar_sprites('assets/jugador/derecha', 8)

def cargar_tiles(ruta):
    tiles = []
    for nombre_archivo in os.listdir(ruta):
        if nombre_archivo.endswith('.png'):
            imagen = pygame.image.load(os.path.join(ruta, nombre_archivo)).convert_alpha()
            imagen = pygame.transform.scale(imagen, (TAMANIO_TILE, TAMANIO_TILE))
            tiles.append(imagen)
    return tiles

tiles_mapa = cargar_tiles('assets/tiles')


mapa = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0]*2,
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0]*2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]*2
]

# Initialize player position and velocity
pos_x = TAMANIO_TILE  # Initial X position
pos_y = ALTO_PANTALLA - 2 * TAMANIO_TILE  # Initial Y position (slightly above the floor)
vel_y = 0
saltando = False
super_salto_cargando = False
indice_sprite = 0

reloj = pygame.time.Clock()

def dibujar_colisiones(mapa, pantalla):
    for fila_idx, fila in enumerate(mapa):
        for col_idx, tile in enumerate(fila):
            if tile != 0:  # Draw only solid tiles
                tile_rect = pygame.Rect(col_idx * TAMANIO_TILE, fila_idx * TAMANIO_TILE, TAMANIO_TILE, TAMANIO_TILE)
                pygame.draw.rect(pantalla, (255, 0, 0), tile_rect, 1)  # Red rectangle for solid tiles

def renderizar_mapa(mapa):
    for fila_idx, fila in enumerate(mapa):
        for col_idx, tile in enumerate(fila):
            if tile != 0:  # Assuming that 0 is an empty space
                pantalla.blit(tiles_mapa[tile - 1], (col_idx * TAMANIO_TILE, fila_idx * TAMANIO_TILE))

def comprobar_colision(mapa, pos_x, pos_y, moviendo_izquierda=False, moviendo_derecha=False, vel_y=0):
    jugador_rect = pygame.Rect(pos_x, pos_y, TAMANIO_TILE_JUGADOR, TAMANIO_TILE_JUGADOR)
    for fila in range(len(mapa)):
        for columna in range(len(mapa[0])):
            if mapa[fila][columna] != 0:  # If the tile is not empty, it's solid
                tile_rect = pygame.Rect(columna * TAMANIO_TILE, fila * TAMANIO_TILE, TAMANIO_TILE, TAMANIO_TILE)
                if jugador_rect.colliderect(tile_rect):  
                    # Collision logic depending on movement direction
                    if moviendo_derecha:
                        jugador_rect.right = tile_rect.left
                    elif moviendo_izquierda:
                        jugador_rect.left = tile_rect.right
                    elif vel_y > 0:  
                        jugador_rect.bottom = tile_rect.top
                    elif vel_y < 0:  
                        jugador_rect.top = tile_rect.bottom
                    vel_y = 0  
                    return tile_rect  
    return None  

jugando = True

while jugando:
    pantalla.blit(FONDO, (0, 0))  
    renderizar_mapa(mapa)  
    dibujar_colisiones(mapa, pantalla)  

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()
    moviendo_izquierda = teclas[pygame.K_LEFT]
    moviendo_derecha = teclas[pygame.K_RIGHT]

    # Horizontal movement
    if moviendo_izquierda:
        nueva_pos_x = pos_x - VELOCIDAD_JUGADOR
        if not comprobar_colision(mapa, nueva_pos_x, pos_y):
            pos_x = nueva_pos_x
            indice_sprite = (indice_sprite + 1) % len(sprites_izquierda)
            pantalla.blit(sprites_izquierda[indice_sprite], (pos_x, pos_y))
    elif moviendo_derecha:
        nueva_pos_x = pos_x + VELOCIDAD_JUGADOR
        if not comprobar_colision(mapa, nueva_pos_x, pos_y):
            pos_x = nueva_pos_x
            indice_sprite = (indice_sprite + 1) % len(sprites_derecha)
            pantalla.blit(sprites_derecha[indice_sprite], (pos_x, pos_y))
    else:
        indice_sprite = (indice_sprite + 1) % len(sprites_parado)
        pantalla.blit(sprites_parado[indice_sprite], (pos_x, pos_y))

    # Super jump mechanic
    if teclas[pygame.K_DOWN]:
        super_salto_cargando = True  
    else:
        if super_salto_cargando:  
            vel_y += SUPER_SALTO_MULTIPLIER * FUERZA_SALTO  
            super_salto_cargando = False  

    # Normal jump mechanic
    if teclas[pygame.K_SPACE] and not saltando:
        vel_y += FUERZA_SALTO  
        saltando = True  

    vel_y += GRAVEDAD  
    nueva_pos_y = pos_y + vel_y  
    colision_tile = comprobar_colision(mapa, pos_x, nueva_pos_y)  

    if colision_tile:
        if vel_y > 0 and pos_y + TAMANIO_TILE_JUGADOR <= colision_tile.top:
            pos_y = colision_tile.top - TAMANIO_TILE  
            vel_y = 0  
            saltando = False  
        else:
            vel_y = 0  
    else:
        pos_y += vel_y  

    # Scroll the map when reaching the top of the screen
    if pos_y < ALTO_PANTALLA / 4:  
        for idx in range(len(mapa)):
            mapa[idx] += [0] * TILES_HORIZONTAL  

    pygame.display.flip()  
    reloj.tick(25)

pygame.quit()