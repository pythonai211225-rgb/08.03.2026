
import random


# ─── Game Logic ──────────────────────────────────────────────────────────────

def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def validate_choice(choice: str) -> bool:
    """Return True if the player's choice is valid."""
    return choice.lower() in ["rock", "paper", "scissors"]


def determine_winner(player: str, computer: str) -> str:
    """Return 'player', 'computer', or 'tie' based on the choices."""
    player = player.lower()
    wins_against = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    if player == computer:
        return "tie"
    elif wins_against[player] == computer:
        return "player"
    else:
        return "computer"


def update_scores(scores: dict, winner: str) -> dict:
    """Return updated scores dict after a round."""
    updated = scores.copy()
    if winner in updated:
        updated[winner] += 1
    return updated


def build_round_summary(player: str, computer: str, winner: str) -> str:
    """Return a formatted string summarising the round result."""
    if winner == "tie":
        result_msg = "It's a tie!"
    elif winner == "player":
        result_msg = "You win this round! 🎉"
    else:
        result_msg = "Computer wins this round! 🤖"
    return (
        f"  You chose   : {player.capitalize()}\n"
        f"  Computer    : {computer.capitalize()}\n"
        f"  Result      : {result_msg}"
    )


def build_score_display(scores: dict) -> str:
    """Return a formatted score string."""
    return (
        f"  Player: {scores['player']}  |  "
        f"Computer: {scores['computer']}  |  "
        f"Ties: {scores['tie']}"
    )


def build_final_message(scores: dict) -> str:
    """Return the final game outcome message."""
    if scores["player"] > scores["computer"]:
        verdict = "🏆 You are the overall winner!"
    elif scores["computer"] > scores["player"]:
        verdict = "💻 Computer is the overall winner!"
    else:
        verdict = "🤝 Overall it's a tie!"
    return verdict


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    scores = {"player": 0, "computer": 0, "tie": 0}

    print("=" * 40)
    print("   Rock  Paper  Scissors")
    print("=" * 40)

    while True:
        print("\nEnter your choice (rock / paper / scissors) or 'quit' to stop:")
        player_choice = input(">>> ").strip().lower()

        if player_choice == "quit":
            break

        if not validate_choice(player_choice):
            print("Invalid choice. Please type rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        scores = update_scores(scores, winner)

        print()
        print(build_round_summary(player_choice, computer_choice, winner))
        print()
        print("  Scores →", build_score_display(scores))

    print("\n" + "=" * 40)
    print("  Final Scores →", build_score_display(scores))
    print(" ", build_final_message(scores))
    print("=" * 40)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
