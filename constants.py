
BSIZ = 3 # board side size

ST_PLAYER = 4 # stones per player

# Define the colors we will use in RGB format
BLACK =   (  0,   0,   0)
GRAY =    (150, 150, 150) 
WHITE =   (255, 255, 255)
# Chosen so that they are still friendly to colorblind people:
BLUISH =  ( 26, 133, 255)
REDDISH = (212,  17,  89)
PLAYER_COLOR = (BLUISH, REDDISH) 

# Define the game window width and height and the slot size and separation in pixels
SLOT = 100        # squares size
SEP = 20          # squares separation
ROOM = SLOT + SEP # extra room at sides 
HEIGHT = BSIZ * SLOT + (BSIZ + 1) * SEP + ROOM # room for 3 squares with margin and internal separators and extra below
WIDTH = HEIGHT + ROOM              # extra at both sides
RAD = SLOT / 3                     # circle radius

NO_PLAYER = -1  #Se usa para representar una casilla vacía en el tablero.
# Durante la inicialización, el tablero se llena con NO_PLAYER, indicando que no hay fichas colocadas.

# Colores para la terminal
COLORES = {
    'NEGRO': '\033[30m',
    'ROJO': '\033[31m',
    'VERDE': '\033[32m',
    'AMARILLO': '\033[33m',
    'AZUL': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'BLANCO': '\033[37m',
    'RESET': '\033[0m',
    'NEGRITA': '\033[1m'
}
