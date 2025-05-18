import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import pandas as pd
from Deck import Deck
from Hand import Hand

# Compute the probability of winning on an early knock in a game of thirty one 
def compute_probability_of_winning(opponent_count, knocking_thresholds, sample_size=1_000_000):
    wins_per_thresholds = [0] * len(knocking_thresholds)
    
    for i in range(len(knocking_thresholds)):
        
        for _ in range(sample_size):
            deck = Deck()
            deck.shuffle()
            
            # lowest for a given sample
            lowest_hand_value = 32

            for _ in range(opponent_count):
                # Deal four cards and keep the best of three since each opponent gets one draw after the knock
                hand = Hand(deck.deal(4))
                hand.keep_best_three()
                hand_value = hand.get_hand_value()
                # Keep track of the lowest hand value for this sample
                lowest_hand_value = hand_value if hand_value < lowest_hand_value else lowest_hand_value
                
            # Track how many wins we get
            if min(lowest_hand_value, knocking_thresholds[i]) != knocking_thresholds[i]:
                wins_per_thresholds[i] += 1

    # Divide our total wins by the sample size to get our win percentage
    probability_of_winning = []
    for i in range(len(knocking_thresholds)):
        probability_of_winning.append(wins_per_thresholds[i] / sample_size * 100)
    
    return probability_of_winning

if __name__ == "__main__":
    opponent_range = list(range(7, 0, -1))  # 7 to 1 Opponents
    knocking_thresholds = list(range(8, 22))  # 8 to 21
    probability_of_winning_per_opponent_count = []
    

    for opponents in opponent_range:
        probability_of_winning = compute_probability_of_winning(opponents, knocking_thresholds)
        print(f"Opponents: {opponents}")
        print(f"  Probability of winning:", probability_of_winning)
        probability_of_winning_per_opponent_count.append(probability_of_winning)

    df = pd.DataFrame(probability_of_winning_per_opponent_count, 
                  index=[o for o in opponent_range],
                  columns=knocking_thresholds)

    df = df.T

    # Sort axes: x high to low, y low to high (already set by you)
    df = df.sort_index(ascending=False)

    # Creating custom heatmap
    colors = [(0.5, 0, 0),       # red
          (1, 0.65, 0),    # orange
          (0.2, 0.5, 0.2)]     # green

    custom_cmap = LinearSegmentedColormap.from_list("custom_heatmap", colors)

    # Plot heatmap with custom cmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, fmt=".2f", cmap=custom_cmap, cbar_kws={'label': 'Probability of Winning'})
    plt.title("Probability of Winning by Knock Threshold and Opponent Count")
    plt.xlabel("Number of Opponents")
    plt.ylabel("Knock Threshold")
    plt.tight_layout()
    plt.show()