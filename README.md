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

### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/main.py">1. main.py</a>  
### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/PlayerDeets.py">2. PlayerDeets.py</a>  
### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/BoardDeets.py">3. BoardDeets.py</a>  
### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/Game.py">4. Game.py</a>  
### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/AI.py">5. AI.py</a> 
### <a href="https://github.com/pradeepkmaran/dots-and-boxes-ai/blob/main/EndGame.py">6. EndGame.py</a> 

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








