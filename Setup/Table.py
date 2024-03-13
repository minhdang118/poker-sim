from Setup.Dealer import Dealer
from Setup.Player import Player


class Table:
    def __init__(self):
        self.players: list[Player] = []
        self.dealer = Dealer()
        self.pot = 0
        self.community_cards = []

    def reset(self):
        self.dealer.reset_deck()
        self.pot = 0
        self.community_cards = []
        for player in self.players:
            player.reset()