from pyray import *
from raylib import *
from game import * 

def boardDeets(playerName):
    rows = 6
    cols = 6

    screen_width = 1920
    screen_height = 1080
    set_target_fps(60)

    input_box_rows = Rectangle(screen_width // 2 - 65, screen_height // 2 - 100, 50, 50)
    input_box_cols = Rectangle(screen_width // 2 + 30, screen_height // 2 - 100, 50, 50)

    rows_text = ""
    cols_text = ""
    active_rows = False
    active_cols = False
    color_inactive = LIGHTGRAY
    color_active = DARKGRAY
    color_rows = color_inactive
    color_cols = color_inactive

    fx_button = load_sound("assets/buttonfx.wav")
    button_disabled = load_texture("assets/enter-button-disabled.png")
    button_open = load_texture("assets/enter-button-open.png")
    button = button_disabled 
    btn_change = True

    frame_height = button.height / 3
    source_rec = [0, frame_height, button.width, frame_height]

    btn_bounds = [screen_width // 2 - button.width // 2 + 10, 
                  screen_height // 2 - 50, 
                  button.width, 
                  frame_height]

    btn_state = 0       # Button state: 0-NORMAL, 1-MOUSE_HOVER, 2-PRESSED
    btn_action = False  # Button action should be activated

    while not window_should_close():
        button = button_disabled
        if is_mouse_button_pressed(0):
            if check_collision_point_rec(get_mouse_position(), input_box_rows):
                active_rows = True
                active_cols = False 
                color_rows = color_active if active_rows else color_inactive
                color_cols = color_active if active_cols else color_inactive
            elif check_collision_point_rec(get_mouse_position(), input_box_cols):
                active_cols = True
                active_rows = False 
                color_rows = color_active if active_rows else color_inactive
                color_cols = color_active if active_cols else color_inactive
            else:
                active_rows = False
                active_cols = False
                color_rows = color_inactive
                color_cols = color_inactive

        if active_rows:
            key = get_key_pressed()
            if key == KEY_BACKSPACE:
                rows_text = rows_text[:-1]
            elif 32 <= key <= 126: 
                rows_text += chr(key)

        if active_cols:
            key = get_key_pressed()
            if key == KEY_BACKSPACE:
                cols_text = cols_text[:-1]
            elif 32 <= key <= 126: 
                cols_text += chr(key)

        if rows_text and cols_text and rows_text.isnumeric() and cols_text.isnumeric():
            button = button_open

        mouse_point = get_mouse_position()
        btn_action = False
        if check_collision_point_rec(mouse_point, btn_bounds):
            if is_mouse_button_down(0):
                btn_state = 2
            else:
                btn_state = 1

            if is_mouse_button_released(0):
                btn_action = True
        else:
            btn_state = 0

        if btn_action:
            try:
                rows = int(rows_text)
                cols = int(cols_text)
                if 1 <= rows < 10 and 1 <= cols < 10:
                    clear_background(RAYWHITE)
                    play_sound(fx_button)
                    game(playerName, rows, cols)
                    break
            except ValueError:
                print("Enter valid number")

        offset_x = -1 if btn_state != 0 else 0
        offset_y = -1 if btn_state != 0 else 0

        begin_drawing()
        clear_background(RAYWHITE)

        draw_text("Enter number of rows (1-9) x columns (1-9):", screen_width//2-200, screen_height // 2 - 130, 20, GRAY)
        draw_rectangle_rec(input_box_rows, color_rows)
        draw_rectangle_lines(int(input_box_rows.x), int(input_box_rows.y), int(input_box_rows.width), int(input_box_rows.height), DARKGRAY)
        draw_text(rows_text, int(input_box_rows.x) + 5, int(input_box_rows.y) + 8, 40, GRAY)

        draw_text("x", screen_width//2-5, screen_height//2-100, 50, GRAY)
        draw_rectangle_rec(input_box_cols, color_cols)
        draw_rectangle_lines(int(input_box_cols.x), int(input_box_cols.y), int(input_box_cols.width), int(input_box_cols.height), DARKGRAY)
        draw_text(cols_text, int(input_box_cols.x) + 5, int(input_box_cols.y) + 8, 40, GRAY)

        draw_texture_rec(button, source_rec, [btn_bounds[0] + offset_x, btn_bounds[1] + offset_y], WHITE)

        if active_rows and (get_time() * 2) % 2 < 1:
            draw_text("_", int(input_box_rows.x) + 8 + measure_text(rows_text, 40), int(input_box_rows.y) + 12, 40, GRAY)
        elif active_cols and (get_time() * 2) % 2 < 1:
            draw_text("_", int(input_box_cols.x) + 8 + measure_text(cols_text, 40), int(input_box_cols.y) + 12, 40, GRAY)

        end_drawing()

    unload_texture(button_disabled)
    unload_texture(button_open)
    close_window() 
