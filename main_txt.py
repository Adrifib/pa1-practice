"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Text handling of a simple tic-tac-toe-like board, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
"""

# Import initialization of the separately programmed abstract board:
from abs_board_h import set_board_up

# Colores
from constants import COLORES

# Importar tiempo
import time

# Limpieza consola
import os

# Prepare board:
# this will set up all stones as unplayed, select a first stone to play,
# and obtain functions to handle them as follows:
#   the call stones() allows one to loop on all stones,
#   the call select_st(i, j) marks as selected the stone at these coordinates,
#   the call move_st(i, j) 
#     if the square at these coordinates is free, moves the selected  
#     stone there, changes player, unselects the stone and checks for 
#     end of game; otherwise, does nothing, leaving the stone selected;
#     returns: bool "stone still selected", next player (may be the same), 
#     and bool "end of game"
#   the call to draw_txt(end) prints a text-based version of the board


def clear():
    # Limpia la pantalla de la consola en windows o linux
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    # Imprime el encabezado del juego
    print(f"\n{COLORES['MAGENTA']}╔══════════════════════╗{COLORES['RESET']}")
    print(f"{COLORES['MAGENTA']}║      TIC TAC TOE     ║{COLORES['RESET']}")
    print(f"{COLORES['MAGENTA']}╚══════════════════════╝{COLORES['RESET']}\n")

def print_turn_indicator(player):
    # Imprime el indicador del turno del jugador actual
    symbol = f"{COLORES['AZUL']}X{COLORES['RESET']}" if player == "x" else f"{COLORES['ROJO']}O{COLORES['RESET']}"
    print(f"{COLORES['MAGENTA']}▶ Turn of {COLORES['RESET']} {symbol}")

def print_input_prompt(message):
    # Imprime un mensaje de solicitud de entrada para el usuario
    print(f"{COLORES['MAGENTA']}► {message}{COLORES['RESET']}", end=" ")

def play_again():
    # Pregunta al usuario si quiere jugar otra vez, y si juega, reinicia el juego, si no imprime el mensaje de despedida
    while True:
        print(f"\n{COLORES['MAGENTA']}Do you want to play again? (y/n):{COLORES['RESET']} ", end="")
        response = input().lower()
        clear()
        if response in ['y', 'n']:
            return response == 'y'
        print(f"{COLORES['ROJO']}Please enter 'y' for yes or 'n' for no.{COLORES['RESET']}")

# Animación de carga del juego
def spinner_bar():
    for i in range(21):
        clear()
        progress = f"{COLORES['AMARILLO']}▰" * i + f"{COLORES['BLANCO']}▱" * (20 - i) + f"{COLORES['AMARILLO']}"
        print(f"{COLORES['AMARILLO']}Loading [{progress}] {i*5}%{COLORES['RESET']}")
        time.sleep(0.1)
    clear()

# Añadido todo dentro de una función para poder reiniciar el juego las veces que sea necesario
def play_game():
    spinner_bar()
    # Prepare board
    stones, select_st, move_st, draw_txt = set_board_up()

    # Initial setup
    stone_selected = True
    curr_player_color = "X"
    end = False

    # Game loop
    print_header()
    draw_txt(end)

    # El try y except sirven para que no pete el juego si no se introduce el valor correcto, y devuelve un mensaje de error, permite seguir jugando
    while not end:
        while not stone_selected:
            print_turn_indicator(curr_player_color)
            print_input_prompt("Select stone coordinates (row col):")
            try:
                i, j = input().split()
                clear()
                print_header()
                stone_selected = select_st(int(i), int(j))
                draw_txt(end)
            except ValueError:
                clear()
                print_header()
                print(f"{COLORES['ROJO']}✘ Invalid input! Please enter two numbers separated by space.{COLORES['RESET']}")
                draw_txt(end)
                continue

        while stone_selected and not end:
            print_turn_indicator(curr_player_color)
            print_input_prompt("Select destination coordinates (row col):")
            try:
                i, j = input().split()
                clear()
                print_header()
                stone_selected, curr_player, end = move_st(int(i), int(j))
                draw_txt(end)
                if not stone_selected:
                    curr_player_color = "0" if curr_player_color == "x" else "x"
            except ValueError:
                clear()
                print_header()
                print(f"{COLORES['ROJO']}✘ Invalid input! Please enter two numbers separated by space.{COLORES['RESET']}")
                draw_txt(end)
                continue

# Bucle principal para ejecutar el juego, si se pregunta y no se quiere volver a jugar, imprime el mensaje de despedida y sale del juego.
while True:
    clear()
    play_game()
    if not play_again():
        clear()
        print(f"\n{COLORES['MAGENTA']}Thank you for playing! See you soon!{COLORES['RESET']}\n")
        break

print(f"\n{COLORES['MAGENTA']}╔══════════════════════╗{COLORES['RESET']}")
print(f"{COLORES['MAGENTA']}║      GAME OVER!      ║{COLORES['RESET']}")
print(f"{COLORES['MAGENTA']}╚══════════════════════╝{COLORES['RESET']}")
input(f"\n{COLORES['MAGENTA']}Press Enter to continue...{COLORES['RESET']}")
clear()






