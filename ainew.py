import sys
import random
import time
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0
    
    def is_fully_expanded(self, all_tex):
        return len(self.children) == len(get_valid_moves(*self.state, all_tex))
    
    def best_child(self, exploration_weight=1.414):
        return max(self.children, key=lambda child: (child.value / (child.visits + 1e-6)) + exploration_weight * (2 * (self.visits ** 0.5) / (child.visits + 1e-6)))

def get_valid_moves(boxes, h_bars, v_bars, all_tex):
    valid_moves = []
    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]:  # gray_h_tex for empty
                valid_moves.append((0, i, j))
    
    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]:  # gray_v_tex for empty
                valid_moves.append((1, i, j))
    
    return valid_moves

def expand_node(node, all_tex):
    valid_moves = get_valid_moves(*node.state, all_tex)
    for move in valid_moves:
        new_state = apply_move(node.state, move, all_tex)
        if new_state not in [child.state for child in node.children]:
            return Node(new_state, parent=node)

def rollout(state, all_tex):
    current_state = state
    while not is_terminal(current_state, all_tex):
        move = random.choice(get_valid_moves(*current_state, all_tex))
        current_state = apply_move(current_state, move, all_tex)
    return get_reward(current_state, all_tex)

def backpropagate(node, reward):
    while node:
        node.visits += 1
        node.value += reward
        node = node.parent

def apply_move(state, move, all_tex):
    boxes, h_bars, v_bars = [[x for x in row] for row in state[0]], [[x for x in row] for row in state[1]], [[x for x in row] for row in state[2]]
    choice, x, y = move
    if choice == 0:
        h_bars[x][y] = all_tex[3]  # blue_h_tex for AI's move
    else:
        v_bars[x][y] = all_tex[4]  # blue_v_tex for AI's move
    updateBoxes(0, boxes, h_bars, v_bars, all_tex)
    return (boxes, h_bars, v_bars)

def is_terminal(state, all_tex):
    boxes, h_bars, v_bars = state
    return sum(findScores(boxes, all_tex)) == len(boxes) * len(boxes[0])

def get_reward(state, all_tex):
    scores = findScores(state[0], all_tex)
    return scores[0] - scores[1]  # AI is assumed to be the first score

def mcts(root, all_tex, time_limit=1.0):
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        node = root
        while node.is_fully_expanded(all_tex) and node.children:
            node = node.best_child()
        
        if not node.is_fully_expanded(all_tex):
            new_child = expand_node(node, all_tex)
            node.children.append(new_child)
            node = new_child
        
        reward = rollout(node.state, all_tex)
        backpropagate(node, reward)
    
    return root.best_child(exploration_weight=0).state

def updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    for i in range(len(boxes)):
        for j in range(len(boxes[0])):
            if (h_bars[i][j] != gray_h_tex and h_bars[i + 1][j] != gray_h_tex and v_bars[i][j] != gray_v_tex and v_bars[i][j + 1] != gray_v_tex):
                if boxes[i][j] == None:
                    if player_turn == 0:
                        boxes[i][j] = blue_win_tex 
                    else:
                        boxes[i][j] = red_win_tex
            else:
                boxes[i][j] = None 

def findScores(boxes, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    ai_score, player_score = 0, 0
    for row in boxes:
        for ele in row:
            if ele == blue_win_tex:
                ai_score += 1
            elif ele == red_win_tex:
                player_score += 1
    return [ai_score, player_score]

def think(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes, h_bars, v_bars = [[x for x in row] for row in boxes_orig], [[x for x in row] for row in h_bars_orig], [[x for x in row] for row in v_bars_orig]
    root = Node((boxes, h_bars, v_bars))
    best_move = mcts(root, all_tex, time_limit=1.0)
    return best_move
