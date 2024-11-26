# Mini Project: Dots and Boxes
**Date :** 12/11/2024
## **Problem Statement:**
 
The goal of this project is to develop an artificial intelligence (AI) system for "Dots and Boxes," a two-player strategy game. This project focuses on implementing AI techniques to create an intelligent opponent for human players and to enable automated gameplay between AI agents.

## **Game Description:** 
Dots and Boxes is played on a grid of dots where players take turns drawing horizontal or vertical lines between adjacent dots. When a player completes a square (box) by drawing the fourth side, they claim it and earn an extra turn. The objective is to claim the most boxes by the end of the game.
## **Project Components:**
### Core Game Logic:
Develop the foundational rules and structure of Dots and Boxes, including the game board setup, move validation, and win conditions.
Ensure that players alternate turns, with each player earning an additional turn upon completing a box.
### AI Integration:
Implement an AI opponent using Alpha-Beta Pruning to optimize decision-making by minimizing possible losses and maximizing gains.
Use an enhanced heuristic evaluation function to analyze board states and choose optimal moves, with strategic considerations for different phases of the game.
### User Interface:
Design a user-friendly graphical interface with Raylib, allowing human players to play against the AI.
Automated Testing for AI Evaluation:
Develop scripts for AI-vs-AI matches to assess the performance of different strategies
and evaluate effectiveness in various game scenarios.
### Project Overview:
This project creates an AI opponent for "Dots and Boxes," a two-player game where players take turns drawing lines on a grid to complete squares. The goal is to claim more squares than the opponent by carefully choosing moves that secure boxes while limiting easy opportunities for the other player. The AI uses smart decision-making methods, such as Alpha-Beta Pruning and Heuristic Evaluation strategies, to play effectively against a human. The board is displayed with red lines for the human player and blue for the AI. Players can choose between playing against the AI or watching two AI opponents play each other.

This project demonstrates how AI can be applied to make strategic moves in turn-based games, providing insights into building challenging, competitive game opponents.
### Game Setup:
#### Board Configuration:
The game is played on a square grid of dots, with board sizes typically set to 3x3, 4x4, or larger, depending on the desired level of complexity. The board is represented as a 2D grid where each line (between dots) is either unmarked, red (human), or blue (AI), indicating which player has claimed that line.
#### Player Roles:
1. There are two players, designated as the Human and the AI.
2. The Human player, using red lines, always starts the game.
3. Players take turns drawing horizontal or vertical lines between adjacent dots.
4. If a player completes a square (box) by drawing the fourth side, they claim that box and earn an extra turn.
5. Players can either be human-controlled or AI-controlled.
6. The setup allows for Human vs. AI flexible testing and interaction.

#### AI Configuration:
The AI uses Alpha-Beta Pruning combined with heuristic evaluation to optimize decision-making. This algorithms enable the AI to analyze the board, choose advantageous moves, and play strategically with efficient computation.

## Key Features
### Board Representation:
The game board is modeled as a 2D array of dots and lines (horizontal and vertical), where each cell represents a square that can be claimed by either player. Each line segment (horizontal or vertical) is tracked to determine whether it has been filled, allowing quick checking of completed squares.
### Player Moves:
The human player (red) and AI (Blue) take turns connecting dots to form lines. When a player completes the fourth line of a square, they claim the box and are rewarded with an extra turn.
The AI uses Alpha-Beta Pruning combined with a heuristic evaluation function to analyze the board and decide on optimal moves.
### AI Algorithms:
#### Alpha-Beta Pruning: 
This algorithm efficiently searches through possible moves by eliminating less promising branches, allowing the AI to evaluate more options within a limited depth.
#### Heuristic Evaluation: 
The heuristic function evaluates the board by scoring the number of claimed boxes, potential future moves, and control over available lines. This scoring helps the AI prioritize moves that maximize its advantage.
### Game Progress and Termination:
The game ends when all boxes on the board are claimed. The player with the most boxes is declared the winner.
A graphical notification shows the winner when the game concludes in Human vs. AI mode.

## Algorithm:
### Algorithm Overview
The AI makes decisions by evaluating each possible move using Alpha-Beta Pruning combined with a Heuristic Evaluation Function. The pruning reduces the number of moves the AI evaluates by cutting off branches that won't improve the outcome, while the heuristic function scores the board states based on desirable configurations, such as control of boxes.

### Algorithm Details
1. **Alpha-Beta Pruning with Minimax:**
Objective: Find the best possible move for the AI while assuming the player also plays optimally.
Alpha-Beta Pruning is applied to eliminate moves that will not influence the outcome, making the algorithm faster.
2. **Heuristic Evaluation Function:**
Since exploring all moves is infeasible, a heuristic function (findScores) estimates board desirability based on AI score, player score, and control score.
\
<br>**Score Components:**<br>
**AI Score:** Increases when the AI claims a box. <br>
**Player Score:** Increases when the player claims a box. <br>
**Control Score:** Counts the number of unfilled boxes, as potential control over boxes is beneficial for future moves.

### Algorithm Steps
```bash
Define Constants:
    Set MAX_DEPTH to limit the depth of recursive search for the Alpha-Beta Pruning. This prevents excessive recursion and keeps decision-making responsive.

Move Evaluation with immediate_move:
    For each move, create copies of the current board (h_bars, v_bars, boxes) to simulate the move without affecting the actual game state.<br>
    Apply the move and update the board with updateBoxes, marking completed boxes for the current player.<br>
    Recur to the next depth level by calling immediate_move with the opposite player.

Alpha-Beta Pruning Logic:
    Track the best scores for both the AI (maximizing player) and the opponent (minimizing player) using alpha and beta.<br>
    For the maximizing player (AI):
        Update best_score if the move improves the score.
        Update alpha with the new best score.
        Prune the branch if alpha >= beta.
    For the minimizing player (player):
        Update best_score if the move reduces the score.
        Update beta with the new best score.
        Prune the branch if beta <= alpha.
    
Generate Available Moves (get_available_moves):
    Collect all unfilled horizontal and vertical bars as potential moves.
    Use these moves to simulate different board states in immediate_move.

Heuristic Evaluation Function (findScores):
    Calculate scores for AI and player by counting boxes they control.
    Include a control score that encourages the AI to aim for potential future moves by favoring unfilled boxes.

Main Decision Function (think_immediate):
    Create copies of the original board to preserve the game state.
    Run immediate_move to get the best move for the AI by evaluating each possible move and selecting the one with the highest score.
```
### Pseudocode Summary
```bash
function think_immediate(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes, h_bars, v_bars = copy(board state)
    best_move, _ = immediate_move(0, boxes, h_bars, v_bars, all_tex)
    return best_move
function immediate_move(player_turn, boxes, h_bars, v_bars, all_tex, depth, alpha, beta):
    if depth == MAX_DEPTH or near endgame:
        return None, findScores(boxes, all_tex)

    best_move, best_score = initialize based on player type
    available_moves = get_available_moves(h_bars, v_bars, all_tex)
    for move in available_moves:
        simulate move on copied board state
        updateBoxes(player_turn, new_boxes, new_h_bars, new_v_bars, all_tex)
        _, score = immediate_move(opposite player, new_boxes, new_h_bars, new_v_bars, all_tex, depth + 1, alpha, beta)

        if maximizing player:
            if score > best_score: update best_score, best_move
            alpha = max(alpha, best_score)
            if beta <= alpha: break
        else:
            if score < best_score: update best_score, best_move
            beta = min(beta, best_score)
            if beta <= alpha: break

    return best_move, best_score

function findScores(boxes, all_tex):
    ai_score, player_score, control_score = calculate from board state
    return ai_score - player_score + 0.5 * control_score

function get_available_moves(h_bars, v_bars, all_tex):
    return list of unfilled bars (moves)
```

### Key Advantages of This Approach
**Efficient Decision-Making**: By integrating Alpha-Beta Pruning into the decision-making process, the AI is able to avoid evaluating every possible move within the game tree. Instead, it eliminates branches that will not influence the final decision. This selective search reduces computational demands, allowing the AI to make decisions faster and freeing up resources to focus on high-impact moves. This efficiency is particularly important as the game progresses, when the number of potential moves may increase exponentially, making a full search impractical without pruning.

**Strategic Move Selection:** The AI’s heuristic evaluation function enables it to make more strategic decisions by weighing not only immediate score impacts but also potential control of the board. For example, the AI considers factors such as the number of tiles it has placed and the positioning of those tiles—favoring central control and clusters of tiles that can limit the opponent's options. By assessing each move in light of these strategic factors, the AI is guided toward choices that have the potential to yield greater long-term advantages, making it more likely to seize control of the game and maintain it.

**Adaptability:** The algorithm’s structure allows the AI to adapt dynamically to various game states and opponent strategies. As each move is evaluated based on the current board setup and the opponent's recent actions, the AI is capable of responding in real time, adjusting its strategy to exploit open areas, reinforce its own advantages, and counter the opponent’s moves. This adaptability ensures that the AI remains competitive and presents a challenging opponent, as it does not rely solely on predefined moves but rather recalibrates its approach continuously throughout the game.
By combining Alpha-Beta Pruning with a nuanced heuristic function that considers both immediate and long-term gains, the AI is equipped to make calculated, strategic decisions that enhance both its efficiency and effectiveness. This approach not only improves game performance but also creates a challenging and engaging experience for the player.

## Modules and Functions:
### pyray and raylib Modules
These modules are used for game development, handling graphics, input, and audio. These are the main modules referenced in the code.
```bash
init_window(screen_width, screen_height, title)
toggle_fullscreen()
init_audio_device()
load_sound(file_name)
load_texture(file_name)
get_mouse_position()
is_mouse_button_down(button)
is_mouse_button_released(button)
clear_background(color)
draw_text(text, x, y, font_size, color)
draw_texture_rec(texture, source_rec, position, color)
begin_drawing()
end_drawing()
set_target_fps(fps)
window_should_close()
check_collision_point_rec(point, rec)
play_sound(sound)
unload_texture(texture)
unload_sound(sound)
close_audio_device()
close_window()
get_key_pressed()
measure_text(text, font_size)
draw_rectangle_rec(rectangle, color)
draw_rectangle_lines(x, y, width, height, color)
```
 ### *PlayerDeets.py* module
 This module handles input for the player's username and moves to the game board setup screen. It has `playerDeets.py` functions that can be used to perform the tasks.

 ### *BoardDeets.py* module
 The function `boardDeets()` is called when the player enters their name and presses the button. It's responsible for setting up the game board.
 
 ### *Game.py* module
 This module is responsible for managing the game logic, handling player and AI turns, detecting valid moves, filling completed boxes, and updating the game state. It alternates turns between the human player (Red) and the AI (Blue), checks for collisions when placing lines, and ends the game when all boxes are filled, displaying the final score. The functions provided by this module are `checkCollision()`, `fillBox()`, `game()`.
 
 ### *AI.py* module
 This module implements a Minimax algorithm with Alpha-Beta Pruning to enable AI decision-making in the Dots and Boxes game. It evaluates the game state by checking available moves, simulating potential moves, and selecting the best move for the AI based on a scoring function. The AI considers up to a maximum depth of 3 for decision-making, balancing between maximizing its score and minimizing the player's score. It provides `think()` function for finding the next move by the computer to play against the human player.
 
 ### *EndGame.py* module
 The module helps to display the game over the screen at the end of a Dots and Boxes game. The screen shows the results (who won or if it's a tie), the score, and two buttons—Play Again and Quit. The player can choose to restart the game or quit the application. It handles button interactions with mouse hover, press, and release states. It returns `endGame()` function that helps display the results of the game.
 
## Source Code:

### 1. Main.py
```python
from pyray import *
from raylib import *
from playerDeets import * 

def main():
    screen_width = 1920
    screen_height = 1080

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

    while not window_should_close():
        mouse_point = get_mouse_position()
        btn_action = False
        
        draw_text("WelcOme tO dOts and bOxes :D", screen_width//2-150, screen_height//2-100, 20, GRAY)

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
```
### 2. PlayerDeets.py
```python
from pyray import *
from raylib import *
from boardDeets import *
from game import *

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
```
### 3. BoardDeets.py
```python
from pyray import *
from raylib import *
from game import * 

def boardDeets(player_name):
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
                    game(player_name, rows, cols)
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

```
### 4. Game.py
```python
import time
from pyray import *
from raylib import *
from ai import think
from endGame import endGame

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
    dot_tex = load_texture("assets/dot.png")
    red_h_tex = load_texture("assets/red-bar-horizontal.png")
    red_v_tex = load_texture("assets/red-bar-vertical.png")
    blue_h_tex = load_texture("assets/blue-bar-horizontal.png")
    blue_v_tex = load_texture("assets/blue-bar-vertical.png")
    gray_h_tex = load_texture("assets/gray-bar-horizontal.png")
    gray_v_tex = load_texture("assets/gray-bar-vertical.png")

    red_win_tex = load_texture("assets/red-win.png")
    blue_win_tex = load_texture("assets/blue-win.png")

    all_tex = [dot_tex, red_h_tex, red_v_tex, blue_h_tex, blue_v_tex, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex]

    screen_width = 1920
    screen_height = 1080

    h_bars = [[gray_h_tex for y in range(col_n)] for x in range(row_n+1)]
    v_bars = [[gray_v_tex for y in range(col_n+1)] for x in range(row_n)]

    start_dot_x = (screen_width//2) - ((col_n//2) * 100) - dot_tex.width//2
    start_dot_y = (screen_height//2) - ((row_n//2) * 100) - dot_tex.height//2

    h_bar_pos = [[Rectangle(start_dot_x + dot_tex.width//2 + x * 100 - 10, start_dot_y + dot_tex.height//2 + y * 100 - 10 ,95, 30,BLACK) for y in range(row_n+1)] for x in range(col_n)]
    v_bar_pos = [[Rectangle(start_dot_x + dot_tex.width//2 + x * 100 - 10, start_dot_y + dot_tex.height//2 + y * 100 - 10, 30, 95,BLACK) for y in range(row_n)] for x in range(col_n+1)]

    boxes = [[None for y in range(col_n)] for x in range(row_n)]

    red_points = 0
    blue_points = 0
    player_turn = True

    while not window_should_close():

        filled_boxes = 0
        for row in boxes:
            for box in row:
                if(box != None):
                    filled_boxes+=1

        if(filled_boxes == row_n * col_n):
            time.sleep(1.5)
            clear_background(WHITE)
            endGame(player_name, red_points, blue_points)
            break

        player_turn = fillBox(boxes, h_bars, v_bars, row_n, col_n, gray_h_tex, gray_v_tex, red_win_tex, blue_win_tex, not player_turn)

        mouse_point = get_mouse_position()
        result = None
        if player_turn and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            result = checkCollision(mouse_point, h_bar_pos, v_bar_pos, row_n, col_n)

        if not player_turn:
            time.sleep(1)
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

        red_points = sum(1 for row in boxes for box in row if box == red_win_tex)
        blue_points = sum(1 for row in boxes for box in row if box == blue_win_tex)

        begin_drawing()
        clear_background(RAYWHITE)

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
        
        if player_turn:
            draw_text("Red Turn", 20, 20, 30, RED)
            draw_text("Blue Turn", 20, 60, 30, GRAY)
        else:
            draw_text("Red Turn", 20, 20, 30, GRAY)
            draw_text("Blue Turn", 20, 60, 30, BLUE)

        draw_text(f"Red Points: {red_points}", 20, 100, 30, RED)
        draw_text(f"Blue Points: {blue_points}", 20, 140, 30, BLUE)

        end_drawing()
```
### 5. AI.py
```python
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
    control_score = sum(1 for row in boxes for box in row if box is None)
    return (ai_score - player_score) + 0.5 * control_score

def immediate_move(player_turn, boxes, h_bars, v_bars, all_tex, depth=0, alpha=float('-inf'), beta=float('inf')):
    if depth == MAX_DEPTH:
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

def think(boxes_orig, h_bars_orig, v_bars_orig, all_tex):
    boxes = [[x for x in row] for row in boxes_orig]
    h_bars = [[x for x in row] for row in h_bars_orig]
    v_bars = [[x for x in row] for row in v_bars_orig]
    
    best_move, _ = immediate_move(0, boxes, h_bars, v_bars, all_tex)
    return best_move 
```
### 6. EndGame.py
```python
import time
from pyray import *
from raylib import *

def endGame(player_name, red_points, blue_points):
    from boardDeets import boardDeets
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
```
## Output Screenshots

#### Title Page View 
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(01).jpeg?raw=true'>

#### Name Page View
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(03).jpeg?raw=true'>

#### Board Dimension Page View
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(04).jpeg?raw=true'>

#### Inital Board Setup
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(05).jpeg?raw=true'>

#### First Move
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(06).jpeg?raw=true'>

#### AI Scores First Point
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(12).jpeg?raw=true'>

#### Players Out Of Moves
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(09).jpeg?raw=true'>

#### Result Page View shows that AI has won the game
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(10).jpeg?raw=true'>

#### Board View of another game with AI
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(17).jpeg?raw=true'>

#### Result Page View of another game with AI
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(18).jpeg?raw=true'>

#### Board View with player leading the game
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(22).jpeg?raw=true'>

#### Result Page View shows that the player and AI has made equal number of points
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(25).jpeg?raw=true'>

#### Result Page View shows that game is tied
<img src='https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/alpha-beta/screenshots/screenshot%20(26).jpeg?raw=true'>

## Conclusion:
The Dots and Boxes AI project demonstrates the effectiveness of using AI to create a challenging and engaging game opponent through a Minimax search algorithm with Alpha-Beta Pruning. By employing this strategy, the AI is able to make strategic decisions that simulate a competitive human player, evaluating potential moves in real-time. The Alpha-Beta Pruning algorithm allows the AI to efficiently explore the game tree, pruning branches that won't affect the outcome, ensuring that the AI can choose optimal moves without the need to examine every possible option.

In addition to the search algorithm, the AI uses a custom-designed heuristic evaluation function that scores the current game state based on factors such as box ownership and control of the board. This evaluation guides the AI to make smart, goal-oriented moves, balancing the pursuit of immediate wins with long-term control of the game.

The project was implemented using Python, with game mechanics and visual elements facilitated by the Raylib library, which made it easy to create a visually engaging and interactive game interface. The AI's decision-making process was refined through extensive testing, including manual evaluation and experimenting with different strategies like the basic Minimax algorithm and the more advanced Minimax with Alpha-Beta Pruning. The final implementation focuses on improving the AI's responsiveness to varying game scenarios, ensuring that it provides a challenging opponent in every game session.

This project highlights the power of AI in board games, delivering a fun and engaging player experience that remains computationally efficient. The flexible structure of the code allows for future expansion, with potential to integrate additional strategies, more complex game variations, or even machine learning-based approaches in the future. The Dots and Boxes AI successfully creates an intelligent opponent while serving as a solid foundation for exploring advanced AI techniques in game development.








