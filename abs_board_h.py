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
from utils import draw_winner_board, draw_winner_txt
from collections import namedtuple
import sys

Stone = namedtuple('Stone', ('x', 'y', 'color'))  # Definir una piedra con sus coordenadas y color

def set_board_up(stones_per_player = ST_PLAYER):
    # Crear una matriz BSIZ x BSIZ (tablero) con todas las casillas marcadas como NO_PLAYER
    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)]
    
    # Inicializar una lista de piedras aún no jugadas (ubicadas fuera del tablero inicialmente)
    # Alterna colores entre los jugadores (PLAYER_COLOR[0] y PLAYER_COLOR[1])
    unplayed = [
        Stone(-1, -1, PLAYER_COLOR[player % 2])  # Coordenadas fuera del tablero (-1, -1)
        for player in range(2 * stones_per_player)  # Crear piedras para ambos jugadores
    ]
    
    # Lista que almacena las piedras que ya han sido colocadas en el tablero
    played = []
    
    # Variable para rastrear al jugador actual (0 o 1)
    curr_player = 0
    
    # Piedra seleccionada para moverse en la fase de movimiento
    selected_stone = None

    def stones():
        # Devuelve un iterador sobre las piedras que ya se han colocado en el tablero
        return iter(played)

    def select_st(i, j):
        nonlocal selected_stone  # Permite modificar la piedra seleccionada en la función externa

        # Verificar que las coordenadas están dentro del tablero y que la casilla pertenece al jugador actual
        if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == curr_player:
            for stone in played:
                # Comprobar si la piedra coincide con las coordenadas y pertenece al jugador actual
                if stone.x == i and stone.y == j and stone.color == PLAYER_COLOR[curr_player]:
                    selected_stone = stone  # Seleccionar la piedra
                    played.remove(stone)  # Eliminar temporalmente la piedra de la lista 'played'
                    return True  # Selección exitosa
        # Si no se selecciona ninguna piedra válida, limpiar la selección
        selected_stone = None
        print("Invalid selection. Please select a valid stone.")  # Mensaje de error
        return False  # Indicar que no se seleccionó ninguna piedra

    def end():
        # Comprobar condiciones de victoria (líneas, columnas o diagonales completas)
        def show_winner(winner):
            if 'main_txt' in sys.modules:
                draw_winner_txt(winner)  # Mostrar el ganador en formato texto si está disponible
            else:
                draw_winner_board(winner)  # Mostrar el ganador en formato gráfico (tablero)

        for i in range(BSIZ):
            # Comprobar si hay una fila completa por un jugador
            if board[i][0] != NO_PLAYER and all(board[i][j] == board[i][0] for j in range(1, BSIZ)):
                show_winner(board[i][0])
                return True, board[i][0]
            # Comprobar si hay una columna completa
            if board[0][i] != NO_PLAYER and all(board[j][i] == board[0][i] for j in range(1, BSIZ)):
                show_winner(board[0][i])
                return True, board[0][i]
        # Comprobar la diagonal principal
        if board[0][0] != NO_PLAYER and all(board[i][i] == board[0][0] for i in range(1, BSIZ)):
            show_winner(board[0][0])
            return True, board[0][0]
        # Comprobar la diagonal inversa
        if board[0][BSIZ-1] != NO_PLAYER and all(board[i][BSIZ-1-i] == board[0][BSIZ-1] for i in range(1, BSIZ)):
            show_winner(board[0][BSIZ-1])
            return True, board[0][BSIZ-1]
        return False, None  # Si no hay ganador, continuar el juego

    def move_st(i, j):
        nonlocal curr_player, selected_stone
        if selected_stone:
            # Mover una piedra seleccionada a una nueva posición si es válida
            if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == NO_PLAYER:
                board[selected_stone.x][selected_stone.y] = NO_PLAYER  # Liberar la casilla anterior
                selected_stone = selected_stone._replace(x=i, y=j)  # Actualizar coordenadas
                played.append(selected_stone)  # Añadir la piedra de nuevo al tablero
                board[i][j] = curr_player  # Marcar la casilla con el jugador actual
                selected_stone = None  # Limpiar la selección
                game_end, winner = end()  # Comprobar si el juego termina
                if game_end:
                    return False, curr_player, True  # El juego terminó con un ganador
                curr_player = 1 - curr_player  # Cambiar al siguiente jugador
                return False, curr_player, False  # Continuar el juego
            print("Invalid move. Stone is still selected.")
            return True, curr_player, False  # Movimiento inválido, la piedra permanece seleccionada

        # Colocar una nueva piedra en el tablero desde la lista de piedras no jugadas
        if unplayed:
            if len(unplayed) > 0:
                stone = unplayed[0]
                if 0 <= i < BSIZ and 0 <= j < BSIZ and board[i][j] == NO_PLAYER:
                    unplayed.pop(0)  # Retirar la piedra de la lista
                    stone = stone._replace(x=i, y=j)  # Asignar las coordenadas
                    played.append(stone)  # Añadirla al tablero
                    board[i][j] = curr_player  # Marcar la casilla
                    game_end, winner = end()  # Comprobar si el juego termina
                    if game_end:
                        return True, curr_player, True
                    curr_player = 1 - curr_player  # Cambiar de jugador
                    return True, curr_player, False
                print("Invalid placement. Try again.")
                return True, curr_player, False  # Colocación inválida

        return False, curr_player, False  # No hay piedras disponibles o el movimiento es inválido

    def draw_txt(end=False):
        # Dibujar el estado actual del tablero en formato texto
        symbols = {NO_PLAYER: ' ', 0: 'O', 1: 'X'}  # Símbolos para representar jugadores y casillas vacías
        print("\n   " + "   ".join(str(i) for i in range(BSIZ)))
        print("  +" + "---+" * BSIZ)
        for i, row in enumerate(board):
            print(f"{i} | " + " | ".join(symbols[cell] for cell in row) + " |")
            print("  +" + "---+" * BSIZ)

    return stones, select_st, move_st, draw_txt  # Retorna las funciones para interactuar con el tablero
