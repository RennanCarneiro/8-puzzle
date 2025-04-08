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
# representa estado da árvore de busca
class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state              # Lista com os números do tabuleiro
        self.parent = parent            # Referência ao nó pai
        self.action = action            # Ação que levou a este estado
        self.depth = depth              # Profundidade no grafo de busca

    # Gera nós filhos com cópia do estado
    def generate_children_copy(self):
        children = []
        zero_index = self.state.index(0)
        for action, move in moves.items():
            if is_valid_move(zero_index, action):
                new_state = deepcopy(self.state)
                new_index = zero_index + move
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                child = Node(new_state, self, action, self.depth + 1)
                children.append(child)
        return children

