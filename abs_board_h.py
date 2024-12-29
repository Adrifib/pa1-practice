"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""

# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY, ST_PLAYER

# Pantalla de ganador
from utils import draw_winner_board

# Data structure for stones
from collections import namedtuple

# Definir estructura de datos para las piedras con coordenadas (x, y) y color
Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player = ST_PLAYER):
    'Init stones and board, prepare functions to provide, act as their closure'

    # Crear el tablero vacío de tamaño BSIZ x BSIZ, con todas las casillas sin jugador (NO_PLAYER)
    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)]
    
    # Inicializar las piedras no jugadas, alternando colores para cada jugador
    unplayed = [
        Stone(-1, -1, PLAYER_COLOR[player % 2])  # Piedra fuera del tablero (-1, -1)
        for player in range(2 * stones_per_player)  # Crear el número de piedras necesarias para ambos jugadores
    ]
    
    # Lista de piedras que ya han sido jugadas en el tablero
    played = []
    
    # Jugador actual (0 o 1, correspondiente al índice en PLAYER_COLOR)
    curr_player = 0
    
    # Piedra seleccionada para mover durante la segunda fase del juego
    selected_stone = None

    def stones():
        """
        return iterable with the stones already played
        Devuelve un iterador con las piedras jugadas
        """
        return iter(played)

    def select_st(i, j):
        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        nonlocal selected_stone  # Acceder a la variable fuera del ámbito local

        # Verificar que la posición está dentro del tablero y pertenece al jugador actual
        if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == curr_player:
            # Buscar la piedra en la lista de jugadas
            for stone in played:
                # Si la piedra está en la posición seleccionada y pertenece al jugador actual
                if stone.x == i and stone.y == j and stone.color == PLAYER_COLOR[curr_player]:
                    selected_stone = stone  # Guardar la piedra seleccionada
                    played.remove(stone)  # Eliminar temporalmente de la lista de piedras jugadas
                    return True  # Devolver True indicando que la piedra fue seleccionada
        selected_stone = None  # Deseleccionar si no se encuentra una piedra válida
        return False  # Devolver False si no se seleccionó ninguna piedra válida

    def end():
        'Test whether there are 3 aligned stones'
        # Comprobar si hay 3 piedras alineadas (filas, columnas o diagonales)
        for i in range(BSIZ):
            # Comprobar filas
            if board[i][0] != NO_PLAYER and all(board[i][j] == board[i][0] for j in range(1, BSIZ)):
                return True, board[i][0]  # Ganador encontrado en fila
            # Comprobar columnas
            if board[0][i] != NO_PLAYER and all(board[j][i] == board[0][i] for j in range(1, BSIZ)):
                return True, board[0][i]  # Ganador encontrado en columna
            # Comprobar diagonal principal
            if board[0][0] != NO_PLAYER and all(board[i][i] == board[0][0] for i in range(1, BSIZ)):
                return True, board[0][0]  # Ganador en diagonal principal
            # Comprobar diagonal secundaria
            if board[0][BSIZ-1] != NO_PLAYER and all(board[i][BSIZ-1-i] == board[0][BSIZ-1] for i in range(1, BSIZ)):
                return True, board[0][BSIZ-1]  # Ganador en diagonal secundaria
        return False, None  # No hay ganador

    def move_st(i, j):
        nonlocal curr_player, selected_stone  # Permitir modificar variables fuera del ámbito local
        
        if selected_stone:  # Si hay una piedra seleccionada
            # Comprobar si la casilla destino está vacía y dentro del tablero
            if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == NO_PLAYER:
                board[selected_stone.x][selected_stone.y] = NO_PLAYER  # Limpiar la casilla anterior
                selected_stone = selected_stone._replace(x=i, y=j)  # Actualizar coordenadas de la piedra
                played.append(selected_stone)  # Reinsertar la piedra en la lista de jugadas
                board[i][j] = curr_player  # Actualizar tablero con el movimiento
                selected_stone = None  # Deseleccionar piedra tras moverla
                game_end, winner = end()  # Comprobar si hay un ganador
                if game_end:
                    draw_winner_board(winner)  # Mostrar pantalla de ganador
                    return False, curr_player, True  # Terminar el juego
                curr_player = 1 - curr_player  # Cambiar turno al siguiente jugador
                return False, curr_player, False
            played.append(selected_stone)  # Reinsertar piedra si el movimiento no es válido
            selected_stone = None  # Deseleccionar piedra
            return False, curr_player, False
        
        if unplayed:  # Si aún quedan piedras no jugadas
            stone = unplayed.pop(0)  # Sacar la siguiente piedra de la lista de piedras no jugadas
            if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == NO_PLAYER:  # Verifica que la posición es válida y está vacía
                 stone = stone._replace(x=i, y=j)  # Actualiza la posición de la piedra (mueve al tablero)
                 played.append(stone)  # Añade la piedra a la lista de piedras jugadas
                 board[i][j] = curr_player  # Actualiza el tablero con la piedra del jugador actual
                 game_end, winner = end()  # Comprueba si alguien ha ganado tras colocar la piedra
                 if game_end:  # Si hay un ganador
                     draw_winner_board(winner)  # Muestra la pantalla del ganador
                     return True, curr_player, True  # Devuelve True indicando que el juego ha terminado
                 curr_player = 1 - curr_player  # Cambia al siguiente jugador si el juego continúa
                 return True, curr_player, False  # Devuelve True, indicando que hay piedra seleccionada y el juego sigue
        return False, curr_player, False  # Devuelve False si no hay piedras no jugadas, manteniendo el estado actual


    def draw_txt(end = False):
        'Use ASCII characters to draw the board.'
        pass

    return stones, select_st, move_st, draw_txt