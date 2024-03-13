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
