from pyray import *
from raylib import *
from BoardDeets import *
from Game import *

def playerDeets():
    screen_width = 1920
    screen_height = 1080
    set_target_fps(60)

    input_box = Rectangle(screen_width // 2 - 200, screen_height // 2 - 100, 400, 50)
    player_name = ""
    active = False
    color_inactive = LIGHTGRAY
    color_active = DARKGRAY
    color = color_inactive

    # Load textures
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
    
    click_text_x, click_text_y = screen_width // 2 - 115, screen_height // 2 - 150 
    enter_text_x, enter_text_y = screen_width // 2 - 115, screen_height // 2 - 130

    btn_state = 0       # Button state: 0-NORMAL, 1-MOUSE_HOVER, 2-PRESSED
    btn_action = False  # Button action should be activated

    while not window_should_close():
        button = button_disabled
        if check_collision_point_rec(get_mouse_position(), input_box):
            if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                active = not active
            color = color_active if active else color_inactive
        else:
            if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                active = not active
                color = color_inactive

        if active:
            key = get_key_pressed()
            if key == KEY_BACKSPACE:
                player_name = player_name[:-1]
            elif 32 <= key <= 126:  
                player_name += chr(key)

        if player_name:
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

        if btn_action and player_name:
            clear_background(RAYWHITE)
            play_sound(fx_button)
            boardDeets(player_name)
            break   

        offset_x = -1 if btn_state != 0 else 0
        offset_y = -1 if btn_state != 0 else 0

        begin_drawing()
        clear_background(RAYWHITE)

        draw_text("Click on the input box!", click_text_x, click_text_y, 20, GRAY)
        draw_text("Enter your username:", enter_text_x, enter_text_y, 20, GRAY)
        draw_rectangle_rec(input_box, color)
        draw_rectangle_lines(int(input_box.x), int(input_box.y), int(input_box.width), int(input_box.height), DARKGRAY)
        draw_text(player_name, int(input_box.x) + 5, int(input_box.y) + 8, 40, GRAY)

        draw_texture_rec(button, source_rec, [btn_bounds[0] + offset_x, btn_bounds[1] + offset_y], WHITE)

        if active:
            if (get_time() * 2) % 2 < 1:
                draw_text("_", int(input_box.x) + 8 + measure_text(player_name, 40), int(input_box.y) + 12, 40, GRAY)

        end_drawing()

    unload_texture(button_disabled)
    unload_texture(button_open)
    close_window()