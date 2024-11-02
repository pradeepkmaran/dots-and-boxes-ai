from pyray import *
from raylib import *
from playerDeets import * 

def main():
    monitor_idx = get_current_monitor()
    monitor_w = get_monitor_width(monitor_idx)
    monitor_h = get_monitor_height(monitor_idx)

    screen_width = 800
    screen_height = 450

    # screen_width = monitor_w
    # screen_height = monitor_h

    init_window(screen_width, screen_height, "dOts and BOxes")
    toggle_fullscreen()
    init_audio_device()

    fx_button = load_sound("assets/buttonfx.wav")
    button = load_texture("assets/start-button-open.png")

    frame_height = button.height / 3
    source_rec = [0, frame_height, button.width, frame_height]

    btn_bounds = [screen_width / 2 - button.width / 2, 
                  screen_height / 2 - button.height / 3 / 2, 
                  button.width, 
                  frame_height]

    btn_state = 0       # Button state: 0-NORMAL, 1-MOUSE_HOVER, 2-PRESSED
    btn_action = False  # Button action should be activated

    set_target_fps(120)

    # Main menu loop
    while not window_should_close():
        mouse_point = get_mouse_position()
        btn_action = False
        
        draw_text("WelcOme tO dOts and bOxes :D", screen_width//3-20, 60, 20, GRAY)

        if check_collision_point_rec(mouse_point, btn_bounds):
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
                btn_state = 2
            else:
                btn_state = 1

            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                btn_action = True
        else:
            btn_state = 0

        offset_x = -1 if btn_state != 0 else 0
        offset_y = -1 if btn_state != 0 else 0

        if btn_action:
            play_sound(fx_button)
            clear_background(RAYWHITE)
            playerDeets()
            break   

        begin_drawing()

        clear_background(RAYWHITE)
        draw_texture_rec(button, source_rec, [btn_bounds[0] + offset_x, btn_bounds[1] + offset_y], WHITE)
        end_drawing()

    unload_texture(button)
    unload_sound(fx_button)

    close_audio_device()
    close_window()

if __name__ == "__main__":
    main()
