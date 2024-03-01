import random

# Card
class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def to_raw_string(self) -> str:
        return self.suit + str(self.value)

    def to_string(self) -> str:

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
            case 10:
                show_value = "T"
            case 11:
                show_value = "J"
            case 12:
                show_value = "Q"
            case 13:
                show_value = "K"
            case _:
                show_value = str(self.value)

        return show_value + show_suit

# Deck
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["h", "d", "c", "s"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

# Dealer
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
    
# Player
class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []
        self.own_chips = 0
        self.bet_chips = 0
        self.folded = False
        self.all_in = False
        
        # List of actions
        # 0: Check
        # 1: Bet
        # 2: Call
        # 3: Raise
        # 4: Fold
        # 5: All-in
        self.actions_allowed = [False, False, False, False, False, False]

    def buy_in(self, buy_in_chips: int):
        self.own_chips = buy_in_chips

    def action_check(self):
        if self.actions_allowed[0]:
            return True
        else:
            return False
    
    def action_bet(self, bet_chips: int):
        if self.actions_allowed[1]:
            self.own_chips -= bet_chips
            self.bet_chips += bet_chips
            return True
        else:
            return False
        
    def action_call(self, call_chips: int):
        if self.actions_allowed[2]:
            self.own_chips -= call_chips
            self.bet_chips += call_chips
            return True
        else:
            return False
        
    def action_raise(self, raise_chips: int):
        if self.actions_allowed[3]:
            self.own_chips -= raise_chips
            self.bet_chips += raise_chips
            return True
        else:
            return False
        
    def action_fold(self):
        if self.actions_allowed[4]:
            self.hand = []
            self.folded = True
            return True
        else:
            return False
    
    def action_all_in(self):
        if self.actions_allowed[5]:
            self.own_chips = 0
            self.bet_chips += self.own_chips
            self.all_in = True
            return True
        else:
            return False
    
    def reset(self):
        self.hand = []
        self.bet_chips = 0
        self.folded = False
        self.all_in = False

# Table
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
    
# Game
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


    
        
    

    
    

    
