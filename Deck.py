import random
from Card import Card

# Regular deck of 54 cards that we can deal from
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

        # Add 2 Jokers
        self.cards.append(Card('Joker', 'Joker'))
        self.cards.append(Card('Joker', 'Joker'))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=1):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards to deal.")
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

    def __len__(self):
        return len(self.cards)

