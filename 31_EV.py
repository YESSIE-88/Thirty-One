import random
import matplotlib.pyplot as plt

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

class Hand:
    def __init__(self, cards):
        if len(cards) != 3:
            raise ValueError("Hand must contain exactly 3 cards.")
        self.cards = cards

    def __repr__(self):
        return f"Hand({self.cards})"
    
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

def compute_expected_hand_value(player_count, sample_size=1_000_000):
    expected_average_hand_value = 0
    expected_minimum_hand_value = 0
    expected_maximum_hand_value = 0

    for _ in range(sample_size):
        deck = Deck()
        deck.shuffle()

        average_hand_value = 0
        minimum_hand_value = 32
        maximum_hand_value = 0
        
        for _ in range(player_count):
            hand = Hand(deck.deal(3))
            hand_value = hand.get_hand_value()
            average_hand_value += hand_value
            minimum_hand_value = hand_value if hand_value < minimum_hand_value else minimum_hand_value
            maximum_hand_value = hand_value if hand_value > maximum_hand_value else maximum_hand_value

        average_hand_value /= player_count
        expected_average_hand_value += average_hand_value
        expected_minimum_hand_value += minimum_hand_value
        expected_maximum_hand_value += maximum_hand_value   

    expected_average_hand_value /= sample_size
    expected_minimum_hand_value /= sample_size
    expected_maximum_hand_value /= sample_size
    
    return expected_average_hand_value, expected_minimum_hand_value, expected_maximum_hand_value

if __name__ == "__main__":
    player_range = list(range(8, 1, -1))  # From 8 to 2
    avg_values = []
    min_values = []
    max_values = []

    for players in player_range:
        avg, min_val, max_val = compute_expected_hand_value(players)
        avg_values.append(avg)
        min_values.append(min_val)
        max_values.append(max_val)

        print(f"Players: {players}")
        print(f"  Average: {avg:.5f}")
        print(f"  Minimum: {min_val:.5f}")
        print(f"  Maximum: {max_val:.5f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(player_range, avg_values, label="Average Hand Value", marker="o")
    plt.plot(player_range, min_values, label="Minimum Hand Value", marker="s")
    plt.plot(player_range, max_values, label="Maximum Hand Value", marker="^")
    plt.xlabel("Number of Players")
    plt.ylabel("Hand Value")
    plt.title("Expected Opening Hand Values by Number of Players")
    plt.legend()
    plt.grid(True)
    plt.xticks(player_range)
    plt.gca().invert_xaxis()  #Show from 8 -> 2 left to right
    plt.tight_layout()
    plt.show()