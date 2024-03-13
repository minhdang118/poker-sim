from Setup.Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["h", "d", "c", "s"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
