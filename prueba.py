def show_winner_menu(winner, root, score_player1=0, score_player2=0):
    """
    Muestra un menú mejorado visualmente que anuncia el ganador del juego.
    
    Args:
        winner (str): El ganador del juego ('X', 'O' o 'Empate')
        root (tk.Tk): La ventana principal
        score_player1 (int): Puntuación del jugador 1
        score_player2 (int): Puntuación del jugador 2
    """
    # Crear una nueva ventana modal
    winner_window = tk.Toplevel(root)
    winner_window.title("¡Fin del juego!")
    winner_window.geometry("400x500")
    winner_window.configure(bg="#f0f0f0")
    
    # Centrar la ventana
    window_width = 400
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    winner_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Hacer la ventana modal
    winner_window.transient(root)
    winner_window.grab_set()
    
    # Frame principal
    main_frame = ttk.Frame(winner_window, padding="20")
    main_frame.pack(expand=True, fill="both")
    
    # Estilo para los widgets
    style = ttk.Style()
    style.configure("Winner.TLabel", font=("Helvetica", 24, "bold"), padding=10)
    style.configure("Score.TLabel", font=("Helvetica", 16), padding=5)
    
    # Mensaje del ganador
    if winner == "Empate":
        winner_text = "¡Es un empate!"
    else:
        winner_text = f"¡Jugador {winner} ha ganado!"
    
    ttk.Label(
        main_frame, 
        text="🏆", 
        font=("Helvetica", 48),
        ).pack(pady=10)
        
    ttk.Label(
        main_frame, 
        text=winner_text,
        style="Winner.TLabel"
        ).pack(pady=10)
    
    # Frame para las puntuaciones
    score_frame = ttk.Frame(main_frame)
    score_frame.pack(pady=20)
    
    ttk.Label(
        score_frame,
        text=f"Jugador X: {score_player1}",
        style="Score.TLabel"
        ).pack()
        
    ttk.Label(
        score_frame,
        text=f"Jugador O: {score_player2}",
        style="Score.TLabel"
        ).pack()
    
    # Botones
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=20)
    
    # Importamos la función del menú principal
    from main_gui import show_menu
    
    # Botón para volver al menú principal
    ttk.Button(
        button_frame,
        text="Volver al menú principal",
        command=lambda: [winner_window.destroy(), show_menu(root)],
        padding=10
    ).pack(pady=10)
    
    # Botón para salir
    ttk.Button(
        button_frame,
        text="Salir del juego",
        command=root.quit,
        padding=10
    ).pack(pady=10)


show_winner_menu(blue, root, score_player1=0, score_player2=0)
