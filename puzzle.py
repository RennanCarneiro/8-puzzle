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

# Busca com profundidade limitada
def depth_limited_search(node, limit):
    if node.state == goal_state:
        return node
    if limit <= 0:
        return None
    for child in node.generate_children_copy():
        result = depth_limited_search(child, limit - 1)
        if result is not None:
            return result
    return None

# Busca Iterativa de Profundidade
def iterative_deepening_search(start_state):
    depth = 0
    while True:
        print(f"Buscando com profundidade limite = {depth}...")
        result = depth_limited_search(Node(start_state), depth)
        if result is not None:
            return result
        depth += 1

# Reconstrói o caminho desde o nó final até o estado inicial
def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    path.reverse()  # Do início até o objetivo
    return path

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])

# Imprime todos os passos desde o estado inicial até o objetivo
def print_solution(goal_node, start_state):
    if goal_node is None:
        print("Nenhuma solução encontrada.")
        return
    path = reconstruct_path(goal_node)
    print(f"\nSolução encontrada em {len(path) - 1} movimentos.\n")
    for i, node in enumerate(path):
        print(f"Movimento {i}: {'Início' if node.action is None else node.action}")
        print_state(node.state)
        print("-----")

# Estado inicial 
start = [1, 2, 3,
         5, 0, 6,
         4, 7, 8]

print("Estado inicial sorteado:")
print_state(start)

start_time = time.time()
goal_node = iterative_deepening_search(start)
end_time = time.time()

print_solution(goal_node, start)
print(f"Tempo de execução: {end_time - start_time:.2f} segundos")

