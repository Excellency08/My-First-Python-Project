import random
import os

try:
    from colorama import Fore, Style, init # type: ignore
    init()
except:
    class Fore:
        RED = GREEN = YELLOW = CYAN = RESET = ""
    class Style:
        RESET_ALL = ""

# Hangman ASCII stages
stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
            |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /     |
            |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
            |
            |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|    |
            |
            |
    =========
    """,
    """
       -----
       |   |
       O   |
       |    |
            |
            |
    =========
    """,
    """
       -----
       |   |
       O   |
            |
            |
            |
    =========
    """,
    """
       -----
       |   |
           |
            |
            |
            |
    =========
    """
]

easy_words = ["cat", "dog", "book", "fish", "tree", "game"]
medium_words = ["python", "laptop", "school", "planet", "garden"]
hard_words = ["programming", "cybersecurity", "developer", "artificial", "algorithm"]

score = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    print(Fore.CYAN + "Select Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter choice: ")

    if choice == "1":
        return random.choice(easy_words)
    elif choice == "2":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

def play_game(chosen_word):

    global score
    display = ["_"] * len(chosen_word)
    lives = 6
    guessed_letters = []

    while lives > 0 and "_" in display:
        clear()
        print(Fore.YELLOW + stages[lives])
        print(Fore.CYAN + "Word: " + " ".join(display))
        print(Fore.GREEN + f"Lives: {lives} | Score: {score}")
        print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.RED + "Invalid input!")
            input("Press Enter...")
            continue

        if guess in guessed_letters:
            print(Fore.RED + "Already guessed!")
            input("Press Enter...")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(Fore.GREEN + "Correct!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
            score += 10
        else:
            lives -= 1
            score -= 5
            print(Fore.RED + "Wrong!")
        
        input("Press Enter...")

    clear()
    if "_" not in display:
        print(Fore.GREEN + "🎉 You Win!")
        print("The word was:", chosen_word)
        score += 20
    else:
        print(Fore.RED + stages[0])
        print("💀 Game Over!")
        print("The word was:", chosen_word)
        score -= 10

def two_player_mode():
    clear()
    print(Fore.CYAN + "Two Player Mode")
    word = input("Player 1, enter a word: ").lower()
    clear()
    play_game(word)


while True:
    clear()
    print(Fore.CYAN + "==== HANGMAN PRO ====")
    print("1. Single Player")
    print("2. Two Player")
    print("3. Exit")

    mode = input("Choose mode: ")

    if mode == "1":
        word = choose_word()
        play_game(word)
    elif mode == "2":
        two_player_mode()
    elif mode == "3":
        break
    else:
        continue

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print(Fore.YELLOW + f"Final Score: {score}")
print("Thanks for playing!")