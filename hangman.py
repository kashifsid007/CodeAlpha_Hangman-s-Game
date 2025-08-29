import random

def hangman():
    # 5 predefined words
    words = ["apple", "train", "house", "river", "chair"]
    word = random.choice(words)  # select random word
    guessed_letters = []  # store guessed letters
    attempts = 6  # allowed wrong guesses
    
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    
    # Create hidden word display
    hidden_word = ["_"] * len(word)
    
    while attempts > 0 and "_" in hidden_word:
        print("\nWord:", " ".join(hidden_word))
        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
            # reveal letter positions
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
    
    # Game result
    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😞 Out of attempts! The word was:", word)

# Run game
hangman()
