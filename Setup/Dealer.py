import random
from Setup.Deck import Deck


class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.shuffle()
    
    def reset_deck(self):
        self.deck = Deck()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck.cards)

    def deal(self):
        return self.deck.cards.pop()
    
    def burn(self):
        self.deck.cards.pop()