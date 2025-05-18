# Thirty-One
This script simulates opening hands in Thirty-One to see how good your first hand usually is.

Goal: 

    This script simulates the opening hand in the card game Thirty-One to determine:

        The expected average value of a starting hand

        The expected minimum value of the lowest hand in each deal

        The expected maximum value of the highest hand in each deal


Background:

    In Thirty-One, each player is dealt 3 cards. The objective is to get a hand of the highest value.
    The maximum value of a hand is 31 hence the name of the game.

    -How a Hand is Valued:

        The value of a hand is the highest sum of the ranks of cards sharing the same suit.

        Alternatively, if all three cards have the same rank, the hand is worth 30.5 points.

    -Card Values:

        Numerical cards are worth their face value.

        Face cards (Jack, Queen, King) are worth 10 points.

        Aces are worth 11 points.

    -Jokers are wild cards, their value depends on the rest of the hand. They take on the role that
    maximizes the hand’s total value:

        They can complete a three-of-a-kind, giving the hand a value of 30.5 points.

        Otherwise, a Joker will act as either an Ace (11 points) or a Face card (10 points) within 
        the most advantageous suit to maximize the hand’s value.

    -Few hand examples with most edge cases:

        king of spades + ace of clubs + two of hearts = 11

        ace of diamonds + queen of diamonds + jack of diamonds = 31

        eight of spades + four of spades + two of diamonds = 12

        three of clubs + three of hearts + three of spades = 30.5

        queen of hearts + ace of spades + joker = 21

        seven of clubs + joker + seven of spades = 30.5

        three of clubs + joker + joker = 30.5

        ace of hearts + joker + joker = 31

    -How the Game Is Played:

        Players take turns drawing either from the deck or the top of the discard pile, aiming 
        to build the highest-value hand possible. After drawing, a player must discard one 
        card, so that they always maintain exactly three cards in hand.

        At any point, a player may "knock"—declaring that they believe their hand is strong 
        enough to avoid being the lowest at the table. Knocking ends the round after each 
        remaining player takes one final turn.

        Knocking immediately after the initial deal—without drawing any cards—is considered a
        risky and aggressive move, as it puts pressure on the rest of the table. This makes
        understanding the statistical value of opening hands critically important, as it
        helps determine whether a hand is strong enough to justify an early knock.


How the script works:

    Randomly shuffles a deck

    Deals 3-card hands to a configurable number of players

    Repeats the process for a configurable number of simulations

    For each round:

        Calculates all players' hand values and Tracks:

            The average hand value across all players in that round

            The lowest hand value in that round

            The highest hand value in that round

    After all rounds, computes and plots:

        The expected average hand value

        The expected minimum of the lowest hand values

        The expected maximum of the highest hand values
