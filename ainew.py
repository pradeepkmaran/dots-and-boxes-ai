import sys
sys.setrecursionlimit(10**6)

# Max depth for the Minimax algorithm
MAX_DEPTH = 5

def updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    for i in range(len(boxes)):
        for j in range(len(boxes[0])):
            if (h_bars[i][j] != gray_h_tex and h_bars[i + 1][j] != gray_h_tex and v_bars[i][j] != gray_v_tex and v_bars[i][j + 1] != gray_v_tex):
                if boxes[i][j] is None:
                    if player_turn == 0:
                        boxes[i][j] = blue_win_tex 
                    else:
                        boxes[i][j] = red_win_tex

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

def count_near_complete_boxes(h_bars, v_bars, gray_h_tex, gray_v_tex):
    near_complete_count = 0
    for i in range(len(h_bars) - 1):
        for j in range(len(v_bars[0]) - 1):
            filled_sides = sum([
                h_bars[i][j] != gray_h_tex,
                h_bars[i+1][j] != gray_h_tex,
                v_bars[i][j] != gray_v_tex,
                v_bars[i][j+1] != gray_v_tex
            ])
            if filled_sides == 3:
                near_complete_count += 1
    return near_complete_count

def minimax(player_turn, depth, boxes, h_bars, v_bars, all_tex, alpha, beta):
    if depth == 0 or sum(findScores(boxes, all_tex)) == len(boxes) * len(boxes[0]):
        ai_score, player_score = findScores(boxes, all_tex)
        score_diff = ai_score - player_score
        near_complete_penalty = count_near_complete_boxes(h_bars, v_bars, all_tex[5], all_tex[6])
        if not player_turn:
            score_diff -= near_complete_penalty  # Discourage moves that set up easy boxes for the player
        return score_diff

    max_score = float('-inf') if not player_turn else float('inf')

    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]:  # Only consider unfilled horizontal bars
                h_bars[i][j] = all_tex[3] if not player_turn else all_tex[1]
                updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex)
                score = minimax(not player_turn, depth - 1, boxes, h_bars, v_bars, all_tex, alpha, beta)
                
                h_bars[i][j] = all_tex[5]  # Reset the bar
                updateBoxes(0, boxes, h_bars, v_bars, all_tex)
                
                if not player_turn:
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                else:
                    max_score = min(max_score, score)
                    beta = min(beta, score)
                
                if beta <= alpha:
                    break  # Prune branches that don't improve the score

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]:  # Only consider unfilled vertical bars
                v_bars[i][j] = all_tex[4] if not player_turn else all_tex[2]
                updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex)
                score = minimax(not player_turn, depth - 1, boxes, h_bars, v_bars, all_tex, alpha, beta)
                
                v_bars[i][j] = all_tex[6]  # Reset the bar
                updateBoxes(0, boxes, h_bars, v_bars, all_tex)
                
                if not player_turn:
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                else:
                    max_score = min(max_score, score)
                    beta = min(beta, score)
                
                if beta <= alpha:
                    break  # Prune branches that don't improve the score

    return max_score

def think(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes, h_bars, v_bars = [[x for x in row] for row in boxes_orig], [[x for x in row] for row in h_bars_orig], [[x for x in row] for row in v_bars_orig]
    best_move = None
    max_score = float('-inf')

    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]:  # Unfilled horizontal bar
                h_bars[i][j] = all_tex[3]
                updateBoxes(False, boxes, h_bars, v_bars, all_tex)
                score = minimax(True, MAX_DEPTH, boxes, h_bars, v_bars, all_tex, float('-inf'), float('inf'))
                
                h_bars[i][j] = all_tex[5]
                updateBoxes(0, boxes, h_bars, v_bars, all_tex)
                
                if score > max_score:
                    max_score = score
                    best_move = [0, i, j]

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]:  # Unfilled vertical bar
                v_bars[i][j] = all_tex[4]
                updateBoxes(False, boxes, h_bars, v_bars, all_tex)
                score = minimax(True, MAX_DEPTH, boxes, h_bars, v_bars, all_tex, float('-inf'), float('inf'))
                
                v_bars[i][j] = all_tex[6]
                updateBoxes(0, boxes, h_bars, v_bars, all_tex)
                
                if score > max_score:
                    max_score = score
                    best_move = [1, i, j]

    return best_move