# Card class with a function to get the point value in thirty one
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # 'Hearts', 'Spades', etc., or 'Joker'
        self.rank = rank  # '2' to 'Ace', or 'Joker'

    def __repr__(self):
        if self.suit == 'Joker':
            return 'Joker'
        return f"{self.rank} of {self.suit}"
    
    def get_point_value(self):
        if self.rank == 'Joker': return 0 # Joker's value will be calculated later
        elif self.rank in ['Jack', 'Queen', 'King']: return 10
        elif self.rank == 'Ace': return 11
        else: return int(self.rank)

