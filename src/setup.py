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

    def deal_hand(self):
        return self.deck.cards.pop()
    
    def burn(self):
        self.deck.cards.pop()
    
    def deal_flop(self):
        return [self.deal(), self.deal(), self.deal()]
    
    def deal_turn(self):
        return self.deal()
    
    def deal_river(self):
        return self.deal()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 0
        self.bet = 0
        self.folded = False
        self.all_in = False

    def add_chips(self, chips):
        self.chips += chips
    
    def bet_chips(self, chips):
        self.chips -= chips
        self.bet += chips
    
    def fold(self):
        self.folded = True
    
    def all_in(self):
        self.all_in = True
    
    def reset(self):
        self.hand = []
        self.bet = 0
        self.folded = False
        self.all_in = False

class Table:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.pot = 0
        self.community_cards = []

    def reset(self):
        self.dealer.reset_deck()
        self.pot = 0
        self.community_cards = []
        for player in self.players:
            player.reset()

    
class Game:
    def __init__(self):
        self.table = Table()
        self.num_players = self.table.players.length
        self.small_blind = 0
        self.big_blind = 0
        self.small_blind_position = 0
        self.big_blind_position = 0
        self.init_blinds()

    def add_player(self, player_name):
        self.table.players.append(player_name)
        self.num_players += 1
    
    def remove_player(self, player_name):
        self.table.players.remove(player_name)
        self.num_players -= 1
    
    def set_blinds(self, small_blind, big_blind):
        self.small_blind = small_blind
        self.big_blind = big_blind

    def init_blinds(self):
        self.small_blind_position = random.randint(0, self.num_players - 1)
        self.big_blind_position = (self.small_blind_position + 1) % self.num_players

    def deal_hands(self):
        for player in self.table.players:
            player.hand.append(self.table.dealer.deal_hand())
            player.hand.append(self.table.dealer.deal_hand())



    def deal_flop(self):
        self.table.dealer.burn()
        self.table.community_cards = self.table.dealer.deal_flop()

    
        
    

    
    

    
