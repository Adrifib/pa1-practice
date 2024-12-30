import os
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinner_dots():
    """Animación de puntos expandiéndose"""
    for _ in range(3):
        for dots in [".", "..", "...", ".....", "..."]:
            clear()
            print(f"Loading{dots}")
            time.sleep(0.2)

def spinner_bar():
    """Barra de progreso simple"""
    for i in range(21):
        clear()
        progress = "▰" * i + "▱" * (20 - i)
        print(f"Loading [{progress}] {i*5}%")
        time.sleep(0.1)

def spinner_rotate():
    """Spinner rotatorio"""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for _ in range(3):
        for char in spinner:
            clear()
            print(f"\r{char} Loading...", end='')
            time.sleep(0.1)

def spinner_bounce():
    """Animación de rebote"""
    for _ in range(3):
        for i in range(0, 20):
            clear()
            spaces = " " * i
            print(f"{spaces}○")
            time.sleep(0.05)
        for i in range(20, 0, -1):
            clear()
            spaces = " " * i
            print(f"{spaces}○")
            time.sleep(0.05)

def loading_game():
    """Simula una pantalla de carga de juego"""
    messages = [
        "Iniciando el juego...",
        "Cargando recursos...",
        "Preparando el tablero...",
        "¡Casi listo!",
        "¡Comenzando!"
    ]
    
    for msg in messages:
        clear()
        print("\n" * 3)
        print(f"  {msg}")
        print("\n" * 3)
        spinner_dots()
        time.sleep(0.3)

def main():
    """Demuestra todas las animaciones"""
    print("Demostración de animaciones de carga\n")
    
    input("Presiona Enter para ver la animación de puntos...")
    spinner_dots()
    
    input("\nPresiona Enter para ver la barra de progreso...")
    spinner_bar()
    
    input("\nPresiona Enter para ver el spinner rotatorio...")
    spinner_rotate()
    
    input("\nPresiona Enter para ver la animación de rebote...")
    spinner_bounce()
    
    input("\nPresiona Enter para ver la pantalla de carga de juego completa...")
    loading_game()
    
    clear()
    print("\n¡Todas las animaciones completadas!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\n\nAnimación interrumpida por el usuario")
        sys.exit(0)
