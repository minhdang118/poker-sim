import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_raw(self):
        print(f"{self.suit}{self.value}", end=" ")

    def show(self):
        show_suit = ""
        show_value = ""

        match self.suit:
            case "h":
                show_suit = "♥"
            case "d":
                show_suit = "♦"
            case "c":
                show_suit = "♣"
            case "s":
                show_suit = "♠"
            case _:
                show_suit = self.suit
        
        match self.value:
            case 1:
                show_value = "A"
            case 11:
                show_value = "J"
            case 12:
                show_value = "Q"
            case 13:
                show_value = "K"
            case _:
                show_value = str(self.value)

        print(f"{show_suit}{show_value}", end=" ")

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["h", "d", "c", "s"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

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
    
    def flop(self):
        return [self.deal(), self.deal(), self.deal()]
    
    def turn(self):
        return self.deal()
    
    def river(self):
        return self.deal()
    
    

    

    
