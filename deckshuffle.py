import numpy as np
import matplotlib.pyplot as plt
import copy

# Create the initial deck
num_cards = 10
num_simulations = 1000000  # Number of simulations

# Shuffle function
def shuffle(deck):
    deck_copy = copy.deepcopy(deck)  # Create a copy of the deck
    start_index = np.random.randint(0, num_cards)
    end_index = np.random.randint(0, num_cards)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    pulled_cards = deck_copy[start_index:end_index]
    remaining_cards = np.delete(deck_copy, np.arange(start_index, end_index))
    new_deck = np.concatenate((pulled_cards, remaining_cards))

    return new_deck

def are_consecutive(x, y):
    return np.abs(x - y) == 1

def is_homogeneous(deck):
    for i in range(len(deck)):
        if are_consecutive(deck[i], deck[(i + 1) % num_cards]):
            return False
    return True

# Simulate the shuffling process multiple times
required_shuffles_values = []
for _ in range(num_simulations):
    current_deck = np.arange(1, num_cards + 1)
    shuffles = 0
    while not is_homogeneous(current_deck):
        current_deck = shuffle(current_deck)
        shuffles += 1
    required_shuffles_values.append(shuffles)

# Create a histogram using matplotlib
bin_width = 5
bins = np.arange(0, max(required_shuffles_values) + bin_width, bin_width)
plt.hist(required_shuffles_values, bins=bins, edgecolor='black')
plt.title("Frequency Distribution of Required Shuffles for a Homogeneous Deck")
plt.xlabel("Number of Required Shuffles")
plt.ylabel("Frequency")
plt.savefig("shuffles_histogram.png")