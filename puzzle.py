import time
from copy import deepcopy

# Estado final desejado
goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]  # 0 representa o espaço vazio

# Movimentos possíveis a partir de qualquer posição
moves = {
    'Cima': -3,
    'Baixo': 3,
    'Esquerda': -1,
    'Direita': 1
}

# Verifica se a movimentação é válida
def is_valid_move(index, direction):
    if direction == 'Esquerda':
        return index % 3 != 0
    elif direction == 'Direita':
        return index % 3 != 2
    elif direction == 'Cima':
        return index >= 3
    elif direction == 'Baixo':
        return index < 6
    return False

