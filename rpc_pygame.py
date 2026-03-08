import random
import pygame
import sys

# ─── Constants ───────────────────────────────────────────────────────────────

WIDTH, HEIGHT = 700, 500
FPS = 60

# Palette
BG        = (15,  15,  25)
CARD_BG   = (28,  28,  45)
ACCENT    = (100, 220, 255)
WHITE     = (240, 240, 255)
GREY      = (120, 120, 150)
WIN_COL   = (80,  220, 130)
LOSE_COL  = (220,  80,  80)
TIE_COL   = (220, 200,  80)

CHOICES = ["rock", "paper", "scissors"]
EMOJI   = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
# Fallback text symbols when emoji font unavailable
SYMBOL  = {"rock": "ROCK", "paper": "PAPER", "scissors": "SCISSORS"}


# ─── Game Logic (same names as original) ─────────────────────────────────────

def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(CHOICES)


def validate_choice(choice: str) -> bool:
    """Return True if the player's choice is valid."""
    return choice in CHOICES


def determine_winner(player: str, computer: str) -> str:
    """Return 'player', 'computer', or 'tie'."""
    wins_against = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if player == computer:
        return "tie"
    return "player" if wins_against[player] == computer else "computer"


def update_scores(scores: dict, winner: str) -> dict:
    """Return updated scores dict after a round."""
    updated = scores.copy()
    if winner in updated:
        updated[winner] += 1
    return updated


def build_round_summary(player: str, computer: str, winner: str) -> str:
    """Return a one-line result string for the HUD."""
    msgs = {"player": "You win! 🎉", "computer": "Computer wins!", "tie": "It's a tie!"}
    return f"{player.upper()}  vs  {computer.upper()}   —   {msgs[winner]}"


def build_score_display(scores: dict) -> str:
    """Return a formatted score string."""
    return (f"You: {scores['player']}    "
            f"CPU: {scores['computer']}    "
            f"Ties: {scores['tie']}")


def build_final_message(scores: dict) -> str:
    """Return the final game outcome message."""
    if scores["player"] > scores["computer"]:
        return "🏆  YOU WIN THE MATCH!"
    elif scores["computer"] > scores["player"]:
        return "💻  COMPUTER WINS THE MATCH!"
    return "🤝  IT'S A DRAW!"


# ─── Drawing helpers ──────────────────────────────────────────────────────────

def draw_button(surface, rect, label, font, hover=False):
    color = ACCENT if hover else CARD_BG
    text_color = BG if hover else WHITE
    pygame.draw.rect(surface, color, rect, border_radius=14)
    pygame.draw.rect(surface, ACCENT, rect, width=2, border_radius=14)
    txt = font.render(label, True, text_color)
    surface.blit(txt, txt.get_rect(center=rect.center))


def draw_card(surface, rect, label, font_big, font_small, highlight=False):
    color = (40, 40, 65) if highlight else CARD_BG
    pygame.draw.rect(surface, color, rect, border_radius=18)
    border_color = ACCENT if highlight else (60, 60, 90)
    pygame.draw.rect(surface, border_color, rect, width=2, border_radius=18)
    txt = font_big.render(SYMBOL[label], True, WHITE)
    surface.blit(txt, txt.get_rect(centerx=rect.centerx, centery=rect.centery - 10))
    sub = font_small.render(label.upper(), True, GREY)
    surface.blit(sub, sub.get_rect(centerx=rect.centerx, centery=rect.bottom - 22))


def result_color(winner: str):
    return {"player": WIN_COL, "computer": LOSE_COL, "tie": TIE_COL}.get(winner, WHITE)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rock  Paper  Scissors")
    clock = pygame.time.Clock()

    font_title  = pygame.font.SysFont("consolas", 32, bold=True)
    font_medium = pygame.font.SysFont("consolas", 18, bold=True)
    font_small  = pygame.font.SysFont("consolas", 13)
    font_card   = pygame.font.SysFont("consolas", 15, bold=True)
    font_big    = pygame.font.SysFont("consolas", 22, bold=True)

    scores = {"player": 0, "computer": 0, "tie": 0}
    state  = "picking"   # "picking" | "result"

    player_choice   = None
    computer_choice = None
    winner          = None

    # Button layout — three choice buttons
    btn_w, btn_h = 160, 70
    gap          = 30
    total_w      = 3 * btn_w + 2 * gap
    start_x      = (WIDTH - total_w) // 2
    btn_y        = 210

    choice_rects = {
        choice: pygame.Rect(start_x + i * (btn_w + gap), btn_y, btn_w, btn_h)
        for i, choice in enumerate(CHOICES)
    }

    play_again_rect = pygame.Rect(WIDTH // 2 - 110, 370, 220, 50)
    reset_rect      = pygame.Rect(WIDTH - 130,  HEIGHT - 55, 110, 38)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if state == "picking":
                    for choice, rect in choice_rects.items():
                        if rect.collidepoint(mouse_pos) and validate_choice(choice):
                            player_choice   = choice
                            computer_choice = get_computer_choice()
                            winner          = determine_winner(player_choice, computer_choice)
                            scores          = update_scores(scores, winner)
                            state           = "result"

                elif state == "result":
                    if play_again_rect.collidepoint(mouse_pos):
                        player_choice   = None
                        computer_choice = None
                        winner          = None
                        state           = "picking"

                if reset_rect.collidepoint(mouse_pos):
                    scores          = {"player": 0, "computer": 0, "tie": 0}
                    player_choice   = None
                    computer_choice = None
                    winner          = None
                    state           = "picking"

        # ── Draw ──────────────────────────────────────────────────────────────
        screen.fill(BG)

        # Title
        title = font_title.render("ROCK  PAPER  SCISSORS", True, ACCENT)
        screen.blit(title, title.get_rect(centerx=WIDTH // 2, y=28))

        # Score bar
        score_txt = font_medium.render(build_score_display(scores), True, WHITE)
        screen.blit(score_txt, score_txt.get_rect(centerx=WIDTH // 2, y=78))

        if state == "picking":
            prompt = font_medium.render("Choose your move:", True, GREY)
            screen.blit(prompt, prompt.get_rect(centerx=WIDTH // 2, y=155))

            for choice, rect in choice_rects.items():
                hover = rect.collidepoint(mouse_pos)
                draw_button(screen, rect, choice.upper(), font_medium, hover)

        elif state == "result":
            # Two result cards side-by-side
            card_w, card_h = 200, 140
            gap_c  = 60
            card_y = 140
            p_rect = pygame.Rect(WIDTH // 2 - gap_c // 2 - card_w, card_y, card_w, card_h)
            c_rect = pygame.Rect(WIDTH // 2 + gap_c // 2,           card_y, card_w, card_h)

            draw_card(screen, p_rect, player_choice,   font_big, font_card, highlight=True)
            draw_card(screen, c_rect, computer_choice, font_big, font_card)

            you_lbl = font_small.render("YOU",      True, ACCENT)
            cpu_lbl = font_small.render("COMPUTER", True, GREY)
            screen.blit(you_lbl, you_lbl.get_rect(centerx=p_rect.centerx, y=card_y - 22))
            screen.blit(cpu_lbl, cpu_lbl.get_rect(centerx=c_rect.centerx, y=card_y - 22))

            # VS divider
            vs = font_medium.render("VS", True, GREY)
            screen.blit(vs, vs.get_rect(center=(WIDTH // 2, card_y + card_h // 2)))

            # Result message
            summary = build_round_summary(player_choice, computer_choice, winner)
            col     = result_color(winner)
            res_txt = font_medium.render(summary, True, col)
            screen.blit(res_txt, res_txt.get_rect(centerx=WIDTH // 2, y=300))

            # Play again button
            hover_pa = play_again_rect.collidepoint(mouse_pos)
            draw_button(screen, play_again_rect, "PLAY AGAIN", font_medium, hover_pa)

        # Reset button (always visible)
        hover_reset = reset_rect.collidepoint(mouse_pos)
        draw_button(screen, reset_rect, "RESET", font_small, hover_reset)

        pygame.display.flip()
        clock.tick(FPS)

    # Final message in terminal after window closes
    print(build_final_message(scores))
    print("Final scores:", build_score_display(scores))
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()