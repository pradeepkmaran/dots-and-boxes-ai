from pyray import *
from raylib import *
from game import *

def boardDeets(player_name):
    game(player_name, 10, 6)
    return

    screen_width = 800
    screen_height = 450
    set_target_fps(60)

    input_box = Rectangle(screen_width // 2 - 200, 220, 400, 50)
    text = ""
    active = False
    color_inactive = LIGHTGRAY
    color_active = DARKGRAY
    color = color_inactive

    # Load textures
    button_disabled = load_texture("assets/enter-button-disabled.png")
    button_open = load_texture("assets/enter-button-open.png")
    button = button_disabled 
    btn_change = True

    frame_height = button.height / 3
    source_rec = [0, frame_height, button.width, frame_height]

    btn_bounds = [screen_width / 2 - button.width / 2, 
                  screen_height * 4 / 5 - button.height / 3 / 2, 
                  button.width, 
                  frame_height]

    btn_state = 0       # Button state: 0-NORMAL, 1-MOUSE_HOVER, 2-PRESSED
    btn_action = False  # Button action should be activated

    while not window_should_close():
        button = button_disabled
        if check_collision_point_rec(get_mouse_position(), input_box):
            if is_mouse_button_pressed(0):
                active = not active
            color = color_active if active else color_inactive
        else:
            active = False
            color = color_inactive

        if active:
            key = get_key_pressed()
            if key == KEY_BACKSPACE:
                text = text[:-1]
            elif 32 <= key <= 126:  
                text += chr(key)

        if text:
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

        if btn_action and text:
            clear_background(RAYWHITE)
            boardDeets()
            break   

        offset_x = -1 if btn_state != 0 else 0
        offset_y = -1 if btn_state != 0 else 0

        begin_drawing()
        clear_background(RAYWHITE)

        draw_text("Click on the input box!", 240, 140, 20, GRAY)
        draw_text("Enter your username:", 240, 170, 20, GRAY)
        draw_rectangle_rec(input_box, color)
        draw_rectangle_lines(int(input_box.x), int(input_box.y), int(input_box.width), int(input_box.height), DARKGRAY)
        draw_text(text, int(input_box.x) + 5, int(input_box.y) + 8, 40, GRAY)

        draw_texture_rec(button, source_rec, [btn_bounds[0] + offset_x, btn_bounds[1] + offset_y], WHITE)

        if active:
            if (get_time() * 2) % 2 < 1:
                draw_text("_", int(input_box.x) + 8 + measure_text(text, 40), int(input_box.y) + 12, 40, GRAY)

        end_drawing()

    # Clean up resources
    unload_texture(button_disabled)
    unload_texture(button_open)
    close_window()  # Close the window after the loop
