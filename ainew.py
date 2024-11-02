import sys
sys.setrecursionlimit(10**6) 

def updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex
    for i in range(len(boxes)):
        for j in range(len(boxes[0])):
            if (h_bars[i][j] and h_bars[i + 1][j] and v_bars[i][j] and v_bars[i][j + 1]):
                if boxes[i][j] == None:
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

def findMaxScore(player_turn, choice, x, y, boxes, h_bars, v_bars, all_tex):
    [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex] = all_tex

    if choice == 0:
        h_bars[x][y] = blue_h_tex if not player_turn else red_h_tex
    else:
        v_bars[x][y] = blue_v_tex if not player_turn else red_v_tex 
    updateBoxes(player_turn, boxes, h_bars, v_bars, all_tex) 

    if sum(findScores(boxes, all_tex)) == len(boxes) * len(boxes[0]):
        return findScores(boxes, all_tex)[0] - findScores(boxes, all_tex)[1] 

    max_score = float('-inf')
    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]: 
                score = findMaxScore(not player_turn, 0, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]: 
                score = findMaxScore(not player_turn, 1, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score

    if choice == 0:
        h_bars[x][y] = all_tex[5] 
    else:
        v_bars[x][y] = all_tex[6] 
    updateBoxes(0, boxes, h_bars, v_bars, all_tex)

    return max_score

def think(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes, h_bars, v_bars = [[x for x in row] for row in boxes_orig], [[x for x in row] for row in h_bars_orig], [[x for x in row] for row in v_bars_orig]
    result = None
    max_score = float('-inf')

    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]: 
                score = findMaxScore(False, 0, i, j, boxes, h_bars, v_bars, all_tex)
                print(score, [0, i, j])
                if score > max_score:
                    max_score = score
                    result = [0, i, j]

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]: 
                score = findMaxScore(False, 1, i, j, boxes, h_bars, v_bars, all_tex)
                print(score, [1, i, j])
                if score > max_score:
                    max_score = score
                    result = [1, i, j]

    return result
