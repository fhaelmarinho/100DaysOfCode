# ✨ 100 Days of Code Challenge - Day 17/100 💻

import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop() if self.deck else None

    def start_game(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card, _ in hand:
            if card in ['Jack', 'Queen', 'King']:
                value += 10
            elif card == 'Ace':
                aces += 1
                value += 11  # Ace can be 1 or 11
            else:
                value += int(card)
        
        while value > 21 and aces:
            value -= 10  # Convert Ace from 11 to 1
            aces -= 1
            
        return value

    def show_hands(self, reveal_dealer=False):
        print("Player's Hand:", self.player_hand, "Value:", self.calculate_hand_value(self.player_hand))
        if reveal_dealer:
            print("Dealer's Hand:", self.dealer_hand, "Value:", self.calculate_hand_value(self.dealer_hand))
        else:
            print("Dealer's Hand: [Hidden]", "Value: [Hidden]")

    def player_turn(self):
        while True:
            self.show_hands()
            action = input("Do you want to (H)it or (S)tand? ").strip().upper()
            if action == 'H':
                card = self.deal_card()
                if card:
                    self.player_hand.append(card)
                    if self.calculate_hand_value(self.player_hand) > 21:
                        print("You busted! Your hand value is over 21.")
                        return False
                else:
                    print("No more cards in the deck!")
                    return False
            elif action == 'S':
                break
            else:
                print("Invalid action. Please choose 'H' or 'S'.")
        return True
    
    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            card = self.deal_card()
            if card:
                self.dealer_hand.append(card)
            else:
                print("No more cards in the deck!")
                break      

def main():
    game = Blackjack()
    game.start_game()
    
    print("Welcome to Blackjack!")
    
    if not game.player_turn():
        game.show_hands(reveal_dealer=True)
        print("Dealer wins!")
        return
    
    game.dealer_turn()
    
    game.show_hands(reveal_dealer=True)
    
    player_value = game.calculate_hand_value(game.player_hand)
    dealer_value = game.calculate_hand_value(game.dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Ponto de entrada
if __name__ == "__main__":
    main()