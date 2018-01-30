import random
import unittest

# SI 206 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time:
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=True):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p2 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code in this section...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):


	# this is a "test"
	def test_create(self):
		card1 = Card()
		self.assertEqual(card1.suit, 'Diamonds')
		self.assertEqual(card1.rank, 2)

	#Test 1:
	def test_queen(self):
		card2 = Card(0 ,12)
		self.assertEqual(card2.rank, 'Queen')

	#Test 2:
	def test_ace(self):
		card3 = Card(0, 1)
		self.assertEqual(card3.rank, 'Ace')

	#Test 3:
	def test_rank_three(self):
		card4 = Card(0, 3)
		self.assertEqual(card4.rank, 3)

	#Test 4:
	def test_clubs(self):
		card5 = Card(1, 1)
		self.assertEqual(card5.suit, 'Clubs')

	#Test 5:
	def test_hearts(self):
		card6 = Card(2, 1)
		self.assertEqual(card6.suit, 'Hearts')

	#Test 6:
	def test_access_var(self):
		card7 = Card(1, 2)
		self.assertEqual(card7.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

	#Test 7:
	def test_string_1(self):
		card8 = Card(2, 7)
		self.assertEqual(card8.__str__(), '7 of Hearts')

	#Test 8:
	def test_string_2(self):
		card9 = Card(3, 13)
		self.assertEqual(card9.__str__(), 'King of Spades')

	#Test 9:
	def test_deck_length(self):
		d1 = Deck()
		self.assertEqual(len(d1.cards), 52)

	#Test 10:
	def test_pop_card_1(self):
		d2 = Deck()
		self.assertEqual(str(d2.pop_card()), 'King of Spades')

	#Test 11:
	def test_pop_card_2(self):
		d3 = Deck()
		d3.pop_card()
		self.assertEqual(len(d3.cards), 51)

	#Test 12:
	def test_replace_card_1(self):
		d4 = Deck()
		c4 = d4.pop_card()
		self.assertEqual(len(d4.cards), 51)
		d4.replace_card(c4)
		self.assertEqual(len(d4.cards), 52)

	#Test 13:
	def test_replace_card_2(self):
		d5 = Deck()
		c5 = d5.replace_card(Card(0, 5))
		self.assertEqual(len(d5.cards), 52)

	#Test 14:
	def test_playwar_1(self):
		self.assertEqual(type(play_war_game()), tuple)

	def test_playwar_2(self):
		game1 = play_war_game()
		self.assertEqual(type(game1[0]), str)

	#additional tests (Tests 15 and 16)
	def test_15(self):
		card15 = Card(1, 10)
		self.assertEqual(card15.__str__(), '10 of Clubs')

	def test_16(self):
		card16 = Card(2, 5)
		self.assertEqual(card16.__str__(), '5 of Hearts')


#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
