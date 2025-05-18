import matplotlib.pyplot as plt
from Deck import Deck
from Hand import Hand

# Compute the expected average, lowest and highest hand value in a game of thirty one 
def compute_expected_hand_value(opponent_count, sample_size=1_000_000):
    
    # Values across all samples
    expected_average_hand_value = 0
    expected_lowest_hand_value = 0
    expected_highest_hand_value = 0

    for _ in range(sample_size):
        deck = Deck()
        deck.shuffle()

        # Values for a given sample
        average_hand_value = 0
        lowest_hand_value = 32
        highest_hand_value = 0
        
        for _ in range(opponent_count):
            # Deal four cards and keep the best of three since each opponent gets one draw after the knock
            hand = Hand(deck.deal(4))
            hand.keep_best_three()
            hand_value = hand.get_hand_value()
            # Keep track of the average, lowest and highest hand value for this sample
            average_hand_value += hand_value
            lowest_hand_value = hand_value if hand_value < lowest_hand_value else lowest_hand_value
            highest_hand_value = hand_value if hand_value > highest_hand_value else highest_hand_value

        # Keep track of the average, lowest and highest hand value across all sample
        average_hand_value /= opponent_count
        expected_average_hand_value += average_hand_value
        expected_lowest_hand_value += lowest_hand_value
        expected_highest_hand_value += highest_hand_value  

    # Compute the expected values by diving by samples size, the higher the sample size, the more accurate
    expected_average_hand_value /= sample_size
    expected_lowest_hand_value /= sample_size
    expected_highest_hand_value /= sample_size
    
    return expected_average_hand_value, expected_lowest_hand_value, expected_highest_hand_value

if __name__ == "__main__":
    opponent_range = list(range(7, 0, -1))  # From 7 to 1 opponents
    avg_values = []
    lowest_values = []
    highest_values = []

    for opponents in opponent_range:
        avg_val, lowest_val, highest_val = compute_expected_hand_value(opponents)
        avg_values.append(avg_val)
        lowest_values.append(lowest_val)
        highest_values.append(highest_val)

        print(f"Opponents: {opponents}")
        print(f"  Average: {avg_val:.5f}")
        print(f"  Minimum: {lowest_val:.5f}")
        print(f"  Maximum: {highest_val:.5f}")

    # Plotting our findings
    plt.figure(figsize=(10, 6))
    plt.plot(opponent_range, avg_values, label="Average Hand Value", marker="o")
    plt.plot(opponent_range, highest_values, label="Lowest Hand Value", marker="s")
    plt.plot(opponent_range, highest_values, label="Highest Hand Value", marker="^")
    plt.xlabel("Number of Opponents")
    plt.ylabel("Hand Value")
    plt.title("Expected Opening Hand + 1 Draw, Values by Number of Opponents")
    plt.legend()
    plt.grid(True)
    plt.xticks(opponent_range)
    plt.gca().invert_xaxis()  #Show from 7 -> 1 left to right
    plt.tight_layout()
    plt.show()