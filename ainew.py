import sys
import copy
import math
sys.setrecursionlimit(10**6)

MAX_DEPTH = 3

def updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    for i in range(len(boxes)):
        for j in range(len(boxes[0])):
            if (h_bars[i][j] != gray_h_tex and h_bars[i + 1][j] != gray_h_tex and 
                v_bars[i][j] != gray_v_tex and v_bars[i][j + 1] != gray_v_tex):
                if boxes[i][j] is None:
                    boxes[i][j] = blue_win_tex if player_turn == 0 else red_win_tex

def findScores(boxes, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    ai_score, player_score = 0, 0
    for row in boxes:
        for ele in row:
            if ele == blue_win_tex:
                ai_score += 1
            elif ele == red_win_tex:
                player_score += 1
    # Calculate control score based on the number of remaining unfilled boxes
    control_score = sum(1 for row in boxes for box in row if box is None)
    return (ai_score - player_score) + 0.5 * control_score

def immediate_move(player_turn, boxes, h_bars, v_bars, all_tex, depth=0, alpha=float('-inf'), beta=float('inf')):
    if depth == MAX_DEPTH or sum(1 for row in boxes for box in row if box is None) <= 4:
        return None, findScores(boxes, all_tex)

    best_move = None
    best_score = float('-inf') if player_turn == 0 else float('inf')
    available_moves = get_available_moves(h_bars, v_bars, all_tex)

    for move in available_moves:
        new_h_bars = [row[:] for row in h_bars] 
        new_v_bars = [row[:] for row in v_bars]
        new_boxes = [row[:] for row in boxes]  

        if move[0] == 0: 
            new_h_bars[move[1]][move[2]] = all_tex[3] if player_turn == 0 else all_tex[1]
        else:
            new_v_bars[move[1]][move[2]] = all_tex[4] if player_turn == 0 else all_tex[2]
        
        updateBoxes(player_turn, new_boxes, new_h_bars, new_v_bars, all_tex)
        
        _, score = immediate_move(1 - player_turn, new_boxes, new_h_bars, new_v_bars, all_tex, depth + 1, alpha, beta)

        if player_turn == 0:
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
        else: 
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_move, best_score

def get_available_moves(h_bars, v_bars, all_tex):
    available_moves = []
    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]:
                available_moves.append([0, i, j])
    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]:
                available_moves.append([1, i, j])
    return available_moves

def think_immediate(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes = [[x for x in row] for row in boxes_orig]
    h_bars = [[x for x in row] for row in h_bars_orig]
    v_bars = [[x for x in row] for row in v_bars_orig]
    
    best_move, _ = immediate_move(0, boxes, h_bars, v_bars, all_tex)
    return best_move 