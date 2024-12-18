import random

# Constants for the number of dice and target score
NUM_DICE = 3
TARGET_SCORE = 50  # Target score to win the game

def roll_dice():
    """
    Simulate rolling three six-sided dice.

    Returns:
        list: A list of three random integers between 1 and 6, representing the dice roll.
    """
    return [random.randint(1, 6) for _ in range(NUM_DICE)]


def check_tupled_out(dice):
    """
    Check if all three dice rolled have the same value, indicating a tuple out.

    Args:
        dice (list): The list of three dice values.

    Returns:
        bool: True if all dice are the same (tupled out), False otherwise.
    """
    return len(set(dice)) == 1


def get_fixed_dice(dice):
    """
    Identify the fixed dice, which are the ones that appear twice (if any).

    Args:
        dice (list): The list of dice rolled.

    Returns:
        list: Indices of the dice that are fixed (appear twice).
    """
    counts = {x: dice.count(x) for x in set(dice)}
    fixed = [i for i, value in enumerate(dice) if counts[value] == 2]
    return fixed


def handle_tupled_out(dice):
    """
    Check for tupled out (all dice same) and return 0 points if true.

    Args:
        dice (list): The list of three dice values.

    Returns:
        int: 0 if tupled out, otherwise None.
    """
    if check_tupled_out(dice):
        print("Tupled out! You score 0 points for this turn.")
        return 0
    return None  # No tupled out, continue with the game


def get_stop_input():
    """
    Prompt the player whether they want to stop or continue re-rolling.

    Returns:
        bool: True if player chooses to stop, False to continue re-rolling.
    """
    stop = input("Do you want to stop? (y/n): ").lower()
    return stop == 'y'


def player_turn(player_num):
    """
    Simulate a player's turn. The player rolls dice, chooses to re-roll or stop, and scores points.

    Args:
        player_num (int): The player's number (starting from 1).

    Returns:
        int: The score for the player's turn (either 0 for tupled out or the sum of the dice if they stop).
    """
    print(f"Player {player_num}'s turn!")
    dice = roll_dice()
    print(f"Initial roll: {dice}")

    # Check for tupled out condition
    score = handle_tupled_out(dice)
    if score == 0:
        return 0  # Player tupled out and scores 0

    total_score = sum(dice)  # Start with the total of the initial roll
    fixed = get_fixed_dice(dice)  # Find which dice are fixed
    rerollable = [i for i in range(NUM_DICE) if i not in fixed]  # Dice that can be re-rolled

    # Continue re-rolling if necessary
    while rerollable:
        rerolled_dice = [
            dice[i] if i in fixed else random.randint(1, 6) for i in range(NUM_DICE)
        ]
        print(f"Re-rolled dice: {rerolled_dice}")
        dice = rerolled_dice  # Update the dice with the re-rolled values

        # Check if the player tupled out after the re-roll
        score = handle_tupled_out(dice)
        if score == 0:
            return 0  # Player tupled out and scores 0

        # Update fixed dice and rerollable dice
        fixed = get_fixed_dice(dice)
        rerollable = [i for i in range(NUM_DICE) if i not in fixed]

        # Ask the player whether they want to stop or continue
        if get_stop_input():
            total_score = sum(dice)  # Player stops, so they score the total of the dice
            print(f"You scored {total_score} points this turn.")
            return total_score

    return total_score


def play_game(num_players=2):
    """
    Main game loop. Players take turns rolling dice until one reaches the target score.
    The game will stop when a player reaches the target score.

    Args:
        num_players (int): The number of players in the game (default is 2).
    """
    scores = [0] * num_players  # Initialize scores for all players
    current_player = 0  # Start with the first player

    # Game loop
    while max(scores) < TARGET_SCORE:
        print(f"Current scores: {scores}")
        score = player_turn(current_player + 1)  # The current player takes their turn
        scores[current_player] += score  # Add score to the player's total
        print(f"Player {current_player + 1}'s total score: {scores[current_player]}")

        # Check if any player has won
        if scores[current_player] >= TARGET_SCORE:
            break

        # Move to the next player
        current_player = (current_player + 1) % num_players

    # Game over, announce the winner
    winner = scores.index(max(scores)) + 1
    print(f"Game Over! Player {winner} wins with {max(scores)} points!")


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    play_game(num_players=num_players)
