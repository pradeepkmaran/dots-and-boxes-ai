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

def findMaxScore(choice, x, y, boxes, h_bars, v_bars, all_tex):
    if sum(findScores(boxes, all_tex)) == len(boxes) * len(boxes[0]):
        return findScores(boxes, all_tex)[0] - findScores(boxes, all_tex)[1] 

    if choice == 0:
        h_bars[x][y] = all_tex[3] 
    else:
        v_bars[x][y] = all_tex[4] 
    updateBoxes(1, boxes, h_bars, v_bars, all_tex) 

    max_score = float('-inf')
    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]: 
                score = findMinScore(0, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]: 
                score = findMinScore(1, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score

    if choice == 0:
        h_bars[x][y] = all_tex[5] 
    else:
        v_bars[x][y] = all_tex[6] 
    updateBoxes(0, boxes, h_bars, v_bars, all_tex)

    return max_score

def findMinScore(choice, x, y, boxes, h_bars, v_bars, all_tex):
    if sum(findScores(boxes, all_tex)) == len(boxes) * len(boxes[0]):
        return findScores(boxes, all_tex)[0] - findScores(boxes, all_tex)[1] 

    if choice == 0:
        h_bars[x][y] = all_tex[1] 
    else:
        v_bars[x][y] = all_tex[2] 
    updateBoxes(0, boxes, h_bars, v_bars) 

    min_score = float('inf')
    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]: 
                score = findMaxScore(0, i, j, boxes, h_bars, v_bars, all_tex)
                if score < min_score:
                    min_score = score

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]: 
                score = findMaxScore(1, i, j, boxes, h_bars, v_bars, all_tex)
                if score < min_score:
                    min_score = score

    if choice == 0:
        h_bars[x][y] = all_tex[5] 
    else:
        v_bars[x][y] = all_tex[6] 
    updateBoxes(1, boxes, h_bars, v_bars)

    return min_score

def think(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes, h_bars, v_bars = boxes_orig[:], h_bars_orig[:], v_bars_orig[:]
    result = None
    max_score = float('-inf')

    for i, row in enumerate(h_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[5]: 
                score = findMaxScore(0, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score
                    result = [0, i, j]

    for i, row in enumerate(v_bars):
        for j, ele in enumerate(row):
            if ele == all_tex[6]: 
                score = findMaxScore(1, i, j, boxes, h_bars, v_bars, all_tex)
                if score > max_score:
                    max_score = score
                    result = [1, i, j]

    return result
