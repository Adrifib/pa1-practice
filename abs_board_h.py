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
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player = 4):
    'Init stones and board, prepare functions to provide, act as their closure'

    # init board and game data here

    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)] # crear el tablero vacío

    unplayed = [
    Stone(-1, -1, PLAYER_COLOR[player % 2])
    for player in range(2 * stones_per_player)
]
    # crear las piedras de los jugadores que aún no han sido jugadas de manera intercalada (ficha en la posición 0 es azul y en la posición 1 es roja y así sucesivamente)

    played = [] # lista de piedras que ya han sido jugadas

    curr_player = 0 # jugador actual


    def stones():
        "return iterable with the stones already played"
        return iter(played)


    def select_st(i, j):
        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        pass


    def end():
        'Test whether there are 3 aligned stones'
        pass

    def move_st(i, j):
        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played;
        if square not valid, do nothing and keep selected stone.
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''
        nonlocal curr_player # para poder modificar la variable curr_player
         
        if 0 <= i < BSIZ and 0 <= j < BSIZ: #comprobar si la piedra esta dentro del tablero
            if board[i][j] == NO_PLAYER and unplayed: # comprobar si la piedra no ha sido jugada y si hay piedras sin jugar
                
                stone = unplayed.pop(0) # sacar la piedra de la lista de piedras sin jugar
                stone = stone._replace(x=i, y=j)  # Actualizar posición
                played.append(stone)  # Añadir a piedras en juego

                board[i][j] = curr_player # actualizar el tablero

                curr_player = 1 - curr_player # cambiar de jugador
            
            return True, curr_player, False # Devolver el estado: piedra siempre seleccionada, jugador actual, fin del juego (false)
        return True, curr_player, False 


    def draw_txt(end = False):
        'Use ASCII characters to draw the board.'
        pass

    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt

