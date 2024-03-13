from Setup.Card import Card


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