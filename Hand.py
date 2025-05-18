from itertools import combinations

# Hand class for a game of Thirty One
class Hand:
    def __init__(self, cards):
        if len(cards) > 4:
            raise ValueError("Hand must contain no more than cards.")
        self.cards = cards

    def __repr__(self):
        return f"Hand({self.cards})"
    
    def keep_best_three(self):
        if len(self.cards) <= 3:
            return  # Nothing to trim
        
        best_value = -1
        best_combo = self.cards[:3]  # default fallback

        for combo in combinations(self.cards, 3):
            test_hand = Hand(list(combo))
            value = test_hand.get_hand_value()
            if value > best_value:
                best_value = value
                best_combo = list(combo)

        self.cards = best_combo
    
    # Check that all non joker cards have the same ranks
    def all_ranks_equal(self):
        ranks = [card.rank for card in self.cards if card.suit != 'Joker']
        return len(ranks) == 0 or all(rank == ranks[0] for rank in ranks)

    # Checks how many a 3 card hand would be worth in the game of 31
    def get_hand_value(self):
        Hearts_value = 0
        Diamonds_value = 0
        Clubs_value = 0
        Spades_value = 0

        thirty_and_a_half = 0

        # Variables for calculating hand values including Jokers
        hand_contains_ace = any(card.rank == 'Ace' for card in self.cards if card.suit != 'Joker')
        num_jokers = sum(1 for card in self.cards if card.suit == 'Joker')

        hand_value = 0
        
        # Calculate the hand value ignoring Jokers
        for card in self.cards:
            if card.suit == 'Hearts':
                Hearts_value += card.get_point_value()
            elif card.suit == 'Diamonds':
                Diamonds_value += card.get_point_value()
            elif card.suit == 'Clubs':
                Clubs_value += card.get_point_value()
            elif card.suit == 'Spades':
                Spades_value += card.get_point_value()

        # If all ranks are equal our hand is worth at least 30.5
        if self.all_ranks_equal(): thirty_and_a_half = 30.5

        # Add the Jokers wild values
        Hearts_value += 10 * num_jokers + int(not(hand_contains_ace))
        Diamonds_value += 10 * num_jokers + int(not(hand_contains_ace))
        Clubs_value += 10 * num_jokers + int(not(hand_contains_ace))
        Spades_value += 10 * num_jokers + int(not(hand_contains_ace))

        hand_value = max(Hearts_value, Diamonds_value, Clubs_value, Spades_value, thirty_and_a_half)

        return hand_value
