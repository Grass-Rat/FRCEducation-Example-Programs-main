import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            else:
                if card.value == "A":
                    aces += 1
                    value += 11
                else:
                    value += 10
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __repr__(self):
        return f"Hand value: {self.get_value()} with cards {', '.join([str(card) for card in self.cards])}"

deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

for _ in range(2):
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

print("Player's hand:", player_hand)
print("Dealer's up card:", dealer_hand.cards[0])

while True:
    action = input("Do you want to 'hit' or 'stand'? ")
    if action.lower() == "hit":
        player_hand.add_card(deck.deal())
        print("Player's hand:", player_hand)
        if player_hand.get_value() > 21:
            print("Player busts! Dealer wins!")
            break
    elif action.lower() == "stand":
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal())
        print("Dealer's hand:", dealer_hand)
        if dealer_hand.get_value() > 21:
            print("Dealer busts! Player wins!")
        elif dealer_hand.get_value() < player_hand.get_value():
            print("Player wins!")
        elif dealer_hand.get_value() > player_hand.get_value():
            print("Dealer wins!")
        else:
            print("It's a tie!")
        break