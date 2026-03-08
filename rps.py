import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").strip().lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if wins_against[player] == computer:
        return "player"
    return "computer"

def display_result(player, computer, result):
    print(f"\nYou chose:      {player}")
    print(f"Computer chose: {computer}")
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "player":
        print("Result: You win! 🎉")
    else:
        print("Result: Computer wins!")

def display_score(player_score, computer_score, ties):
    print(f"\n--- Score ---")
    print(f"You:      {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties:     {ties}")
    print("-------------")

def play_game():
    player_score = 0
    computer_score = 0
    ties = 0

    print("=== Rock Paper Scissors ===\n")

    while True:
        player = get_player_choice()

        if player == "quit":
            print("\nThanks for playing!")
            display_score(player_score, computer_score, ties)
            break

        computer = get_computer_choice()
        result = determine_winner(player, computer)
        display_result(player, computer, result)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1

        display_score(player_score, computer_score, ties)
        print()


if __name__ == "__main__":
    play_game()