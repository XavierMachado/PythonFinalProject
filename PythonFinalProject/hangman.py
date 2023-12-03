# Import necessary modules
import random
import pickle
from words import word_list

# Function to get a random word from the word list
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Hangman Game class
class HGame:
    def __init__(self, user_name):
        self.user_name = user_name
        self.round_number = 1
        self.wins = 0
        self.losses = 0

    # Method to play a round of Hangman
    def play_round(self):
        word = get_word()
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print(self.display_hangman(tries))
        print(" ".join(word_completion))
        print("\n")
        
        # Main game loop
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            # Handling letter guesses
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            # Handling word guesses
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(self.display_hangman(tries))
            print(" ".join(word_completion))
            print("\n")
        
        # Handling game result
        if guessed:
            print("Congrats, you guessed the word! You win!")
            result = "win"
            self.wins += 1
            self.round_number += 1
            return result
        else:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
            result = "lose"
            self.losses += 1
            self.round_number += 1
            return result

    # Method to display the hangman based on remaining tries
    def display_hangman(self, tries):
        stages = [  # Hangman ASCII art
            # final state: head, torso, both arms, and both legs
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # head, torso, both arms, and one leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # head, torso, and both arms
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # head, torso, and one arm
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # head and torso
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # head
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            # initial empty state
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[tries]

    # Method to display game statistics
    def display_statistics(self):
        print(f"{self.user_name}, here are your game play statistics...")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        if self.losses > 0:
            win_loss_ratio = round(self.wins / self.losses, 2)
        else:
            win_loss_ratio = self.wins
        print(f"Win/Loss Ratio: {win_loss_ratio}")

    # Method to save the game state
    def save_game(self):
        with open(f"{self.user_name}.hang", "wb") as file:
            pickle.dump(self, file)
        file.close()

# Function to load a saved game
def load_game(user_name):
    try:
        with open(f"{user_name}.hang", "rb") as file:
            game = pickle.load(file)
            game.round_number = game.wins + game.losses + 1
            return game
    except FileNotFoundError:
        print(f"{user_name}, your game could not be found.")
        return None

