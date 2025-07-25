import random
import time

def print_welcome():
    print("=" * 50)
    print("🦑 Welcome to Glass Stepping Stones 🦑".center(50))
    print("=" * 50)
    print("Choose wisely between [L]eft or [R]ight at each step.")
    print("You have 3 lives. One wrong step and you fall!")
    print()

def get_safe_side():
    return random.choice(["L", "R"])

def take_step(choice, safe_side):
    return choice.upper() == safe_side

def play_game():
    lives = 3
    level = 1

    while lives > 0:
        safe_side = get_safe_side()
        choice = input(f"Level {level} - Choose [L] or [R]: ").strip().upper()

        if choice not in ["L", "R"]:
            print("❗ Invalid choice. Please enter 'L' or 'R'.")
            continue

        if take_step(choice, safe_side):
            print("✅ You survived this step!")
            level += 1
        else:
            lives -= 1
            print("💥 You chose wrong! You lost a life.")
            print(f"❤️ Lives left: {lives}\n")

    print("☠️ GAME OVER. You fell from the glass bridge!")
    print(f"🏆 You reached level {level}.")
