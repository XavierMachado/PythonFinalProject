from rps import RPSGame, load_game as load_rps_game
from hangman import HGame, load_game as load_hangman_game
from guessnumber import GuessNumberGame, load_game as load_guess_number_game
from mastermind import MastermindGame, load_game as load_mastermind_game
from blackjack import BlackjackGame, load_game as load_blackjack_game

# Function to get the user's name
def get_user_name():
    return input("What is your name? ")

# Function to prompt the user to load a previous game or start a new one
def load_or_new_game(create_new_game, load_game_function, user_name, game_type):
    while True:
        load_option = input(f"Do you want to load a previous {game_type} game? (y/n): ").lower()
        if load_option == "y":
            # Attempt to load a previous game
            game = load_game_function(user_name)
            if game:
                print(f"Welcome back {user_name}. Let's continue playing {game_type}!\n")
                return game
            else:
                print("Please try again, and make sure your name is correct.")
                # If loading fails, prompt the user again
                choose_game(create_new_game, load_game_function, game_type)
        elif load_option == "n":
            # Create a new game
            game = create_new_game(user_name)
            print(f"Hello {user_name}. Let's play {game_type}!\n")
            return game
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Function to handle the game selection and gameplay loop
def choose_game(create_new_game, load_game_function, game_type):
    user_name = get_user_name()
    game = load_or_new_game(create_new_game, load_game_function, user_name, game_type)

    while True:
        result = game.play_round()
        print("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Save and Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            # Start a new game
            game = create_new_game(user_name)
            print(f"Hello {game.user_name}. Let's play {game_type} again!\n")
        elif choice == "2":
            # Display game statistics
            game.display_statistics()
            print("\nWhat would you like to do?\n1. Play Again\n2. View Statistics\n3. Save and Quit")
            choice = input("Enter choice: ")
            if choice == "3":
                # Save the game and exit
                game.save_game()
                print(f"{game.user_name}, your {game_type} game has been saved.")
                exit()
        elif choice == "3":
            # Save the game and exit
            game.save_game()
            print(f"{game.user_name}, your {game_type} game has been saved.")
            exit()

if __name__ == "__main__":
    print("Welcome to the Game Station!\n" + "Choose a game to play from the options below!")
    print("1. Rock, Paper, Scissors\n2. Hangman\n3. Guess the Number\n4. Mastermind\n5. Blackjack\n6. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        choose_game(RPSGame, load_rps_game, "Rock, Paper, Scissors")
    elif choice == "2":
        choose_game(HGame, load_hangman_game, "Hangman")
    elif choice == "3":
        choose_game(GuessNumberGame, load_guess_number_game, "Guess the Number")
    elif choice == "4":
        choose_game(MastermindGame, load_mastermind_game, "Mastermind")
    elif choice == "5":
        choose_game(BlackjackGame, load_blackjack_game, "Blackjack")
    elif choice == "6":
        exit()
