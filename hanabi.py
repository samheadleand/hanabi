#!/usr/bin/python3

import collections
import random

# Format of card:
	# Set of Tuples
# Five lists keep track of 
# Players hand -> 

#cards_played

COLOURS = {'white', 'blue', 'yellow', 'red', 'green'}
NUMBERS = list(range(1, 6))
COUNT = {1: 3, 2: 2, 3: 2, 4: 2, 5: 1}

CARDS = collections.Counter({
		(colour, number): COUNT[number]
			for colour in COLOURS
			for number in NUMBERS
})

PLAYER1 = 1
PLAYER2 = 2

initial_cards = list(CARDS.elements())
played_cards = []
discarded_cards = []
player1_cards = []
player2_cards = []



class Hanabi:
	def __init__(self):
		self.unused_cards = list(CARDS.elements())
		self.played_cards = []
		self.discarded_cards = []
		self.player1_cards = []#self.initial_pickup()
		self.player2_cards = []#self.initial_pickup()
	def pickup_card(self, player):
		card = random.choice(self.unused_cards)
		self.unused_cards.remove(card)
		if player == PLAYER1:
			self.player1_cards.append(card)
		elif player == PLAYER2:
			self.player2_cards.append(card)
	def get_players_cards(self, player):
		if player == PLAYER1:
			return self.player1_cards
		elif player == PLAYER2:
			return self.player2_cards
	def get_unused_cards(self):
		return self.unused_cards

	
game = Hanabi()
game.pickup_card(PLAYER1)
print (game.get_players_cards(PLAYER1))
print (game.get_unused_cards())





