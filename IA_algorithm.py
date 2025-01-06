# Función para verificar si un jugador ha ganado
def check_winner(board, player):
    # Combinaciones ganadoras: filas, columnas y diagonales
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6],             # Diagonales
    ]
    
    # Comprobamos cada combinación ganadora
    for combo in winning_combinations:
        # Si todas las posiciones de la combinación están ocupadas por el jugador,
        # significa que este jugador ha ganado
        if all(board[i] == player for i in combo):
            return True
    # Si no se encuentra ninguna combinación ganadora, retornamos False
    return False

# Función para verificar si el juego ha terminado en empate
def is_draw(board):
    # Si todas las casillas están ocupadas y no hay ganador, es empate
    return all(cell != "" for cell in board)

# Implementación del algoritmo Minimax
def minimax(board, depth, is_maximizing):
    # Si la IA ha ganado, devuelve una puntuación positiva (cuanto más baja la profundidad, mejor)
    if check_winner(board, "O"):  # IA gana
        return 10 - depth
    # Si el jugador ha ganado, devuelve una puntuación negativa (cuanto más baja la profundidad, peor)
    if check_winner(board, "X"):  # Jugador gana
        return depth - 10
    # Si no hay más movimientos (empate)
    if is_draw(board):  # Empate
        return 0

    if is_maximizing:  # Es el turno de la IA (Maximizar la puntuación)
        # Inicializamos la mejor puntuación con un valor muy bajo
        best_score = -float("inf")
        
        # Recorremos todas las casillas del tablero
        for i in range(len(board)):
            # Si la casilla está vacía, probamos un movimiento
            if board[i] == "":
                board[i] = "O"  # Simula el movimiento de la IA
                score = minimax(board, depth + 1, False)  # Llamada recursiva para el siguiente turno (del jugador)
                board[i] = ""  # Deshacemos el movimiento
                best_score = max(score, best_score)  # Mantenemos el mejor puntaje
        return best_score
    else:  # Es el turno del jugador (Minimizar la puntuación)
        # Inicializamos la mejor puntuación con un valor muy alto
        best_score = float("inf")
        
        # Recorremos todas las casillas del tablero
        for i in range(len(board)):
            # Si la casilla está vacía, probamos un movimiento
            if board[i] == "":
                board[i] = "X"  # Simula el movimiento del jugador
                score = minimax(board, depth + 1, True)  # Llamada recursiva para el siguiente turno (de la IA)
                board[i] = ""  # Deshacemos el movimiento
                best_score = min(score, best_score)  # Mantenemos el peor puntaje
        return best_score

# Función para encontrar el mejor movimiento para la IA
def find_best_move(board):
    # Inicializamos la mejor puntuación con un valor muy bajo
    best_score = -float("inf")
    best_move = None
    
    # Recorremos todas las casillas del tablero
    for i in range(len(board)):
        # Si la casilla está vacía, probamos un movimiento
        if board[i] == "":
            board[i] = "O"  # Simula el movimiento de la IA
            score = minimax(board, 0, False)  # Llamada al algoritmo Minimax para obtener la puntuación de esta jugada
            board[i] = ""  # Deshacemos el movimiento
            # Si esta jugada es mejor que las anteriores, la guardamos
            if score > best_score:
                best_score = score
                best_move = i  # Guardamos la posición de la mejor jugada
    return best_move  # Retorna la mejor jugada encontrada
