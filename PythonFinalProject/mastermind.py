# Import necessary modules
import random
import pickle

# Mastermind Game class
class MastermindGame:
    def __init__(self, user_name):
        # Initialize game attributes
        self.user_name = user_name
        # Generate a random secret code of 4 colors ('R', 'G', 'B', 'Y')
        self.secret_code = [random.choice(['R', 'G', 'B', 'Y']) for _ in range(4)]
        self.attempts = 0
        self.record_attempts = float('inf')

    # Method to play a round of Mastermind
    def play_round(self):
        while True:
            guess = input("Enter your guess (e.g., RGBY): ").upper()

            # Validate the guess format
            if len(guess) != 4 or not all(color in 'RGBY' for color in guess):
                print("Invalid guess. Please enter a 4-letter code using 'R', 'G', 'B', and 'Y'.")
                continue

            # Increment the number of attempts
            self.attempts += 1
            # Evaluate the guess and provide feedback
            feedback = self.evaluate_guess(guess)

            print(f"Attempt {self.attempts}: {guess}  Feedback: {feedback}")

            # Check if the guess is correct
            if guess == ''.join(self.secret_code):
                print(f"Congratulations! You guessed the code {guess} in {self.attempts} attempts.")

                # Check for a new record in the least number of attempts
                if self.attempts < self.record_attempts:
                    self.record_attempts = self.attempts
                    print(f"New record! The previous record was {self.record_attempts} attempts.")

                break

    # Method to evaluate a guess and provide feedback
    def evaluate_guess(self, guess):
        feedback = []
        for i in range(4):
            if guess[i] == self.secret_code[i]:
                feedback.append('Correct')
            elif guess[i] in self.secret_code:
                feedback.append('Wrong position')
            else:
                feedback.append('Incorrect')

        return ', '.join(feedback)

    # Method to display game statistics
    def display_statistics(self):
        print(f"Mastermind Game Statistics for {self.user_name}:")
        print(f"Record for the least number of guesses: {self.record_attempts}")

    # Method to save the game state
    def save_game(self):
        with open(f"{self.user_name}.mind", "wb") as file:
            pickle.dump(self, file)

# Function to load a saved game
def load_game(user_name):
    try:
        with open(f"{user_name}.mind", "rb") as file:
            game = pickle.load(file)
            return game
    except FileNotFoundError:
        print(f"{user_name}, your Mastermind game could not be found.")
        return None
