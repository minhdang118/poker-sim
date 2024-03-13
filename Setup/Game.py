import random
from Setup.Player import Player
from Setup.Table import Table


class Game:
    def __init__(self):
        self.table = Table()
        self.num_players = len(self.table.players)
        self.players_in_game = self.table.players
        self.max_bet = 0
        self.max_raise = 0
        self.small_blind = 0
        self.big_blind = 0
        self.small_blind_position = 0
        self.big_blind_position = 0
    
    def reset(self):
        self.table.reset()
        self.num_players = len(self.table.players)
        self.players_in_game = self.table.players
        self.max_bet = 0
        self.max_raise = 0
        self.small_blind = 0
        self.big_blind = 0
        self.small_blind_position = 0
        self.big_blind_position = 0

    def add_player(self, player: Player):
        self.table.players.append(player)
        self.num_players += 1
    
    def remove_player(self, player_name: str):
        for player in self.table.players:
            if player.name == player_name:
                self.table.players.remove(player)
        self.num_players -= 1
    
    def set_blinds(self, small_blind: int, big_blind: int):
        self.small_blind = small_blind
        self.big_blind = big_blind

    def init_blinds(self):
        self.small_blind_position = random.randint(0, self.num_players - 1)
        self.big_blind_position = (self.small_blind_position + 1) % self.num_players
    
    def change_blinds(self):
        self.small_blind_position = (self.small_blind_position + 1) % self.num_players
        self.big_blind_position = (self.big_blind_position + 1) % self.num_players

    def set_action(self):
        if self.max_bet == 0:
            for player in self.players_in_game:
                if player.own_chips == 0:
                    player.actions_allowed = [True, False, False, False, True, False]
                else:
                    player.actions_allowed = [True, True, False, False, True, True]
        else:
            for player in self.players_in_game:
                if player.own_chips == 0:
                    player.actions_allowed = [False, False, False, False, True, False]
                elif 0 < player.bet_chips < self.max_bet:
                    player.actions_allowed = [False, False, False, False, True, True]
                elif self.max_bet <= player.bet_chips < (self.max_bet + self.max_raise):
                    player.actions_allowed = [False, False, True, False, True, True]
                else:
                    player.actions_allowed = [False, False, True, True, True, True]
            

    def deal_hands(self):
        for player in self.table.players:
            player.hand.append(self.table.dealer.deal())
            player.hand.append(self.table.dealer.deal())
            
    def deal_flop(self):
        self.table.dealer.burn()
        for _ in range(3):
            self.table.community_cards.append(self.table.dealer.deal())
        
    def deal_turn(self):
        self.table.dealer.burn()
        self.table.community_cards.append(self.table.dealer.deal())
    
    def deal_river(self):
        self.table.dealer.burn()
        self.table.community_cards.append(self.table.dealer.deal())