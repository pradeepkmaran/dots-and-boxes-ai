from pyray import *
from raylib import *
from ainew import think

def checkCollision(mouse_point, h_bar_pos, v_bar_pos, row_n, col_n):
    for x in range(col_n):
        for y in range(row_n + 1):
            bar_rect = h_bar_pos[x][y]
            if check_collision_point_rec(mouse_point, bar_rect):
                return [0, y, x] 

    for x in range(col_n + 1):
        for y in range(row_n):
            bar_rect = v_bar_pos[x][y]
            if check_collision_point_rec(mouse_point, bar_rect):
                return [1, y, x] 
    return None

def fillBox(boxes, h_bars, v_bars, row_n, col_n, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex, player_turn):
    ok = 0
    for x in range(col_n):
        for y in range(row_n):
            if(boxes[y][x] == None):
                if(h_bars[y][x] != gray_h_tex and h_bars[y+1][x] != gray_h_tex and v_bars[y][x] != gray_v_tex and v_bars[y][x+1] != gray_v_tex):
                    ok = 1
                    if(player_turn):
                        boxes[y][x] = red_win_tex
                    else:
                        boxes[y][x] = blue_win_tex
    if ok:
        return player_turn
    return not player_turn

def game(player_name, row_n, col_n):
    dot_tex = load_texture("assets/game/dot.png")
    red_h_tex = load_texture("assets/game/bars/red-bar-horizontal.png")
    red_v_tex = load_texture("assets/game/bars/red-bar-vertical.png")
    blue_h_tex = load_texture("assets/game/bars/blue-bar-horizontal.png")
    blue_v_tex = load_texture("assets/game/bars/blue-bar-vertical.png")
    gray_h_tex = load_texture("assets/game/bars/gray-bar-horizontal.png")
    gray_v_tex = load_texture("assets/game/bars/gray-bar-vertical.png")


    red_win_tex = load_texture("assets/game/red-win.png")
    blue_win_tex = load_texture("assets/game/blue-win.png")

    all_tex = [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex]

    screen_width = 800
    screen_height = 450

    h_bars = [[gray_h_tex for y in range(col_n)] for x in range(row_n+1)]
    v_bars = [[gray_v_tex for y in range(col_n+1)] for x in range(row_n)]

    start_dot_x = (screen_width//2) - ((col_n//2) * 100)
    start_dot_y = (screen_height//2) - ((row_n//2) * 100)    

    offset = 240

    h_bar_pos = [[Rectangle(start_dot_x + offset + x * 100, start_dot_y + offset+ y * 100, 95, 30,BLACK) for y in range(row_n+1)] for x in range(col_n)]
    v_bar_pos = [[Rectangle(start_dot_x + offset + x * 100, start_dot_y +offset + y * 100, 30, 95,BLACK) for y in range(row_n)] for x in range(col_n+1)]

    boxes = [[None for y in range(col_n)] for x in range(row_n)]

    player_turn = True

    while not window_should_close():

        player_turn = fillBox(boxes, h_bars, v_bars, row_n, col_n, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex, not player_turn)

        mouse_point = get_mouse_position()
        result = None
        if player_turn and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            result = checkCollision(mouse_point, h_bar_pos, v_bar_pos, row_n, col_n)

        if not player_turn:
            result = think(boxes, h_bars, v_bars, all_tex)

        if result is not None:
            if result[0] == 0:
                if h_bars[result[1]][result[2]] == gray_h_tex:
                    h_bars[result[1]][result[2]] = red_h_tex if player_turn else blue_h_tex
                    player_turn = not player_turn
            else:
                if v_bars[result[1]][result[2]] == gray_v_tex:
                    v_bars[result[1]][result[2]] = red_v_tex if player_turn else blue_v_tex
                    player_turn = not player_turn

        begin_drawing()
        for x in range(col_n+1):
            for y in range(row_n+1):
                pos_x = start_dot_x + x * 100
                pos_y = start_dot_y + y * 100
                draw_texture(dot_tex, pos_x, pos_y, WHITE)

        for x in range(col_n):
            for y in range(row_n+1):
                pos_x = start_dot_x + x * 100 + 50
                pos_y = start_dot_y + y * 100
                draw_texture(h_bars[y][x], pos_x, pos_y, WHITE)

        for x in range(col_n+1):
            for y in range(row_n):
                pos_x = start_dot_x + x * 100
                pos_y = start_dot_y + y * 100 + 50
                draw_texture(v_bars[y][x], pos_x, pos_y, WHITE)    

        for x in range(col_n):
            for y in range(row_n):
                if(boxes[y][x] != None):
                    pos_x = start_dot_x + x * 100 + 50
                    pos_y = start_dot_y + y * 100 + 50
                    draw_texture(boxes[y][x], pos_x, pos_y, WHITE)

        end_drawing()