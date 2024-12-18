Tuple Out Dice Game
Description: 
The Tuple Out Dice Game is a simple dice-based game where players take turns rolling three six-sided dice. The goal is to score points by rolling the dice and avoiding a "tuple out" (where all three dice show the same number). Players can choose to re-roll any dice that are not fixed (those that appear twice) until they either stop and score the points or "tuple out," in which case they score 0 points for the round.

Rules:
Each player rolls three dice.
If all three dice show the same number (tupled out), the player scores 0 points for the turn.
If two dice have the same value, those dice are considered "fixed" and cannot be re-rolled.
Players can choose to stop re-rolling and keep the points based on the sum of the dice rolled.
If a player opts to re-roll the remaining dice, they continue until they either stop or "tuple out."
The game ends when one player reaches the target score (default is 50).

Features:
Multi-player support (default: 2 players).
Players can choose to stop re-rolling or continue to maximize their points.
The game ends when a player reaches the target score.
The game checks for "tuple out" after each roll and updates the score accordingly.
Requirements:
Python 3.x

How to Play:
1. Clone the repository:
Copy code
git clone https://github.com/Miggy-byte/INST126-Word-Count.git
2. Run the game:
In your terminal, navigate to the directory containing the script and run it with the following command:

Copy code
python tuple_out_dice_game.py
3. Game Flow:
The game will prompt you to enter the number of players at the start.
Each player will take turns rolling the dice. On each turn, the game will show the result of the dice roll, ask if you want to stop or continue re-rolling, and calculate the score.
The game continues until one player reaches or exceeds the target score (default: 50 points).
The game announces the winner once a player reaches the target score.
Code Structure
Functions:
roll_dice(): Simulates rolling three six-sided dice.
check_tupled_out(dice): Checks if all three dice show the same number (tuple out).
get_fixed_dice(dice): Identifies the dice that are fixed (those that appear twice).
handle_tupled_out(dice): Handles the case where a player tupled out and scored 0 points.
get_stop_input(): Prompts the player if they want to stop re-rolling the dice.
player_turn(player_num): Simulates a player's turn, including rolling, re-rolling, and scoring.
play_game(num_players=2): Main game loop where players take turns, and the game continues until one player reaches the target score.
