import random

def hangman():
    words = ["python", "code", "alpha", "intern", "program"]
    word = random.choice(words)  # Randomly select a word
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("🎮 Welcome to Hangman Game!")
    print("Word to guess:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if guess in used_letters:
            print("You already guessed that letter!")
            continue

        used_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        print("Word:", " ".join(guessed))

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("😢 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
