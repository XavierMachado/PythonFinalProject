# Import necessary modules
import random
import pickle

# Blackjack Game class
class BlackjackGame:
    def __init__(self, user_name):
        # Initialize game attributes
        self.user_name = user_name
        self.player_hand = []
        self.dealer_hand = []
        self.is_game_over = False
        self.player_wins = 0
        self.dealer_wins = 0

    # Method to deal a random card
    def deal_card(self):
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return random.choice(cards)

    # Method to calculate the score of a hand
    def calculate_score(self, hand):
        score = 0
        num_aces = 0

        for card in hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                num_aces += 1
            else:
                score += int(card)

        for _ in range(num_aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score

    # Method to play a round of Blackjack
    def play_round(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.is_game_over = False

        while not self.is_game_over:
            print(f"Your cards: {self.player_hand}, current score: {self.calculate_score(self.player_hand)}")
            print(f"Dealer's first card: {self.dealer_hand[0]}")

            if self.calculate_score(self.player_hand) == 21:
                print("Blackjack! You win!")
                self.is_game_over = True
            elif self.calculate_score(self.player_hand) > 21:
                print("Bust! You went over 21. You lose.")
                self.is_game_over = True
            else:
                user_input = input("Type 'y' to get another card, 'n' to pass: ").lower()
                if user_input == "y":
                    new_card = self.deal_card()
                    self.player_hand.append(new_card)
                    print(f"You drew a {new_card}.")
                    if self.calculate_score(self.player_hand) > 21:
                        print("Bust! You went over 21. You lose.")
                        self.is_game_over = True
                else:
                    self.is_game_over = True

        while self.calculate_score(self.dealer_hand) < 17:
            new_card = self.deal_card()
            self.dealer_hand.append(new_card)
            print(f"Dealer drew a {new_card}.")

        print(f"Your final hand: {self.player_hand}, final score: {self.calculate_score(self.player_hand)}")
        print(f"Dealer's final hand: {self.dealer_hand}, final score: {self.calculate_score(self.dealer_hand)}")

        # Determine the winner based on the scores
        if self.calculate_score(self.player_hand) > 21:
            print("You lose! Your score is over 21.")
            self.dealer_wins += 1
        elif self.calculate_score(self.dealer_hand) > 21:
            print("Dealer bust! You win!")
            self.player_wins += 1
        elif self.calculate_score(self.player_hand) > self.calculate_score(self.dealer_hand):
            print("You win!")
            self.player_wins += 1
        elif self.calculate_score(self.player_hand) < self.calculate_score(self.dealer_hand):
            print("You lose.")
            self.dealer_wins += 1
        else:
            print("It's a draw!")

    # Method to save the game state
    def save_game(self):
        with open(f"{self.user_name}.jack", "wb") as file:
            pickle.dump(self, file)

    # Method to display game statistics
    def display_statistics(self):
        print(f"{self.user_name}, here are your game play statistics...")
        print(f"Player Wins: {self.player_wins}")
        print(f"Dealer Wins: {self.dealer_wins}")

# Function to load a saved game
def load_game(user_name):
    try:
        with open(f"{user_name}.jack", "rb") as file:
            game = pickle.load(file)
            return game
    except FileNotFoundError:
        print(f"{user_name}, your game could not be found.")
        return None
