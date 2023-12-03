import random
import pickle

class RPSGame:
    def __init__(self, user_name):
        self.user_name = user_name
        self.round_number = 1
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def play_round(self):
        print(f"Round {self.round_number}\n")
        print("1. Rock\n2. Paper\n3. Scissors\n")
        user_choice = self.get_user_choice()
        computer_choice = random.randint(1, 3)
        self.display_choices(user_choice, computer_choice)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_statistics(result)
        self.round_number += 1
        return result

    def get_user_choice(self):
        while True:
            try:
                user_choice = int(input("What will it be? "))
                if user_choice in [1, 2, 3]:
                    return user_choice
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")

    def display_choices(self, user_choice, computer_choice):
        choices = ["Rock", "Paper", "Scissors"]
        print(f"You chose {choices[user_choice - 1]}. The computer chose {choices[computer_choice - 1]}.")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            return "win"
        else:
            return "lose"

    def update_statistics(self, result):
        if result == "win":
            self.wins += 1
        elif result == "lose":
            self.losses += 1
        else:
            self.ties += 1

    def display_statistics(self):
        print(f"{self.user_name}, here are your game play statistics...")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Ties: {self.ties}")
        if self.losses > 0:
            win_loss_ratio = round(self.wins / self.losses, 2)
        else:
            win_loss_ratio = self.wins
        print(f"Win/Loss Ratio: {win_loss_ratio}")

    def save_game(self):
        with open(f"{self.user_name}.rps", "wb") as file:
            pickle.dump(self, file)
        file.close()
            
def load_game(user_name):
    try:
        with open(f"{user_name}.rps", "rb") as file:
            game = pickle.load(file)
            game.round_number = game.wins + game.losses + game.ties + 1
            return game
    except FileNotFoundError:
        print(f"{user_name}, your game could not be found.")
        return None

"""def main():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("1. Start New Game\n2. Load Game\n3. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        user_name = input("What is your name? ")
        game = RPSGame(user_name)
        print(f"Hello {user_name}. Let's play!\n")

    elif choice == "2":
        user_name = input("What is your name? ")
        game = load_game(user_name)
        if game:
            print(f"Welcome back {user_name}. Let's play!\n")
        else:
            main()
            return

    elif choice == "3":
        exit()

    while True:
        result = game.play_round()
        print("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            game.display_statistics()
            print("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Quit")
            choice = input("Enter choice: ")
            if choice == "3":
                game.save_game()
                print(f"{game.user_name}, your game has been saved.")
                exit()
        elif choice == "3":
            game.save_game()
            print(f"{game.user_name}, your game has been saved.")
            exit()

main()"""
