import random

# Deck of 52 cards
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

def initial_deal():
	hand = []
	# Each player initially starts with 7 cards
	while len(hand) < 7:
		deck_index = random.randint(0, int(len(deck)-1))
		hand.append(deck[deck_index])
		del deck[deck_index]

	return hand

print initial_deal()
print initial_deal()
