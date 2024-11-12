import time
from pyray import *
from raylib import *

def endGame(player_name, red_points, blue_points):
    from BoardDeets import boardDeets
    screen_width = 1920
    screen_height = 1080
    
    fx_button = load_sound("assets/buttonfx.wav")
    play_again_button = load_texture("assets/play-again-button.png")
    quit_button = load_texture("assets/quit-button.png")

    button_width = 230
    button_height = 80

    play_again_source_rec = [play_again_button.width/2 - button_width/2, play_again_button.height/2-button_height/2, button_width, button_height]
    quit_source_rec = [quit_button.width/2- button_width/2, quit_button.height/2-button_height/2, button_width, button_height]

    play_again_btn_bounds = [screen_width // 2 - button_width // 2, 
                             screen_height * 2 / 3 - button_height / 2, 
                             button_width, button_height]

    quit_btn_bounds = [screen_width // 2 - button_width // 2, 
                       screen_height * 2 / 3 - button_height / 2 + 130, 
                       button_width, button_height]

    play_again_btn_state = 0
    quit_btn_state = 0

    set_target_fps(60)

    while not window_should_close():
        mouse_point = get_mouse_position()
        
        result_text = ""
        if red_points > blue_points:
            result_text = f"{player_name} Wins!"
        elif red_points < blue_points:
            result_text = "AI Wins!"
        else:
            result_text = "It's a Tie!"

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text(f"Game Over", screen_width // 2 - 100, screen_height // 2 - 150, 40, GRAY)
        draw_text(result_text, screen_width // 2 - 100, screen_height // 2 - 100, 30, DARKGRAY)
        draw_text(f"Red Points: {red_points}", screen_width // 2 - 100, screen_height // 2 - 30, 20, RED)
        draw_text(f"Blue Points: {blue_points}", screen_width // 2 - 100, screen_height // 2, 20, BLUE)

        if check_collision_point_rec(mouse_point, play_again_btn_bounds):
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
                play_again_btn_state = 2
            else:
                play_again_btn_state = 1
            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                clear_background(WHITE)
                boardDeets(player_name) 
                break
        else:
            play_again_btn_state = 0

        if check_collision_point_rec(mouse_point, quit_btn_bounds):
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
                quit_btn_state = 2
            else:
                quit_btn_state = 1
            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                play_sound(fx_button) 
                close_window()
                break
        else:
            quit_btn_state = 0

        offset_x_play_again = -1 if play_again_btn_state != 0 else 0
        offset_y_play_again = -1 if play_again_btn_state != 0 else 0
        draw_texture_rec(play_again_button, play_again_source_rec, 
                         [play_again_btn_bounds[0] + offset_x_play_again, 
                          play_again_btn_bounds[1] + offset_y_play_again], WHITE)
        
        offset_x_quit = -1 if quit_btn_state != 0 else 0
        offset_y_quit = -1 if quit_btn_state != 0 else 0
        draw_texture_rec(quit_button, quit_source_rec, 
                         [quit_btn_bounds[0] + offset_x_quit, 
                          quit_btn_bounds[1] + offset_y_quit], WHITE)
        
        end_drawing()

    unload_texture(play_again_button)
    unload_texture(quit_button)
    close_window()
