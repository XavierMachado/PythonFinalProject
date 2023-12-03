# Import necessary modules
import random
import pickle

# Guess the Number Game class
class GuessNumberGame:
    def __init__(self, user_name):
        # Initialize game attributes
        self.user_name = user_name
        self.round_number = 1
        self.wins = 0
        self.losses = 0
        self.max_guesses = 7

    # Method to play a round of Guess the Number
    def play_round(self):
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        guesses = 0

        print("Welcome to Guess the Number!")
        print(f"I've selected a number between 1 and 100. Try to guess it in {self.max_guesses} tries.")

        # Main game loop
        while guesses < self.max_guesses:
            try:
                print(f"Number of guesses used: {guesses}\n")
                # Get user's guess
                user_guess = int(input("Enter your guess: "))
                guesses += 1

                # Check if the guess is correct
                if user_guess == number_to_guess:
                    print(f"Congratulations, {self.user_name}! You guessed the number {number_to_guess} in {guesses} tries.")
                    result = "win"
                    self.wins += 1
                    self.round_number += 1
                    break
                # Provide hints for incorrect guesses
                elif user_guess < number_to_guess:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")

            # Handle invalid input (non-numeric)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        else:
            # If the user runs out of guesses
            print(f"Sorry, {self.user_name}. You ran out of guesses. The correct number was {number_to_guess}.")
            result = "lose"
            self.losses += 1
            self.round_number += 1

        return result

    # Method to display game statistics
    def display_statistics(self):
        print(f"{self.user_name}, here are your game play statistics...")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")

    # Method to save the game state
    def save_game(self):
        with open(f"{self.user_name}.guess", "wb") as file:
            pickle.dump(self, file)
        file.close()

# Function to load a saved game
def load_game(user_name):
    try:
        with open(f"{user_name}.guess", "rb") as file:
            game = pickle.load(file)
            game.round_number = game.wins + game.losses + 1
            return game
    except FileNotFoundError:
        print(f"{user_name}, your game could not be found.")
        return None
