import random
import time

#creating an object representing a separate card. it has the suit and values
class Card:

    def __init__(self, suit, value): 
        self.suit = suit 
        self.value = value

    def getTextValue(self):
        if self.value < 11:
              return self.value
        elif self.value == 11:
              return "Jack"
        elif self.value == 12:
              return "Queen"
        elif self.value == 13:
              return "King"
        elif self.value == 14:
              return "Ace"
      
    #returns the string representing the card's value
    def __str__(self):
          return self.getTextValue()
    
    #represents a Card object in a readable way (a string)
    def __repr__(self):
          value = self.getTextValue()
          return f"{value} of {suit}"

#creating class Hand. (cards that the user and robot have)		
class Hand:
	def __init__(self):
		self.cards = []
	def calculateHandValue(self):
		totalValue = 0
		for card in self.cards:
			totalValue += card.value
		return totalValue
	def getStatus(self):
		handValue = self.calculateHandValue()
		print(f"The hand is {len(self.cards)} card(s) : {self.cards} which equals to {handValue} points.")	
	def takeCard(self, card):
		self.cards.append(card)

#creating an object for the main deck of cards
class Deck:
        def __init__(self):
              self.cards = []
        def removeCard(self):
              card = self.cards.pop()
              return card
        def addCard(self, card):
              self.cards.append(card)
        def shuffle(self):
              random.shuffle(self.cards)
            
suits = ["Spades ♠️ ", "Diamonds ♦️ ", "Clubs ♣️ ", "Hearts ♥️ "]
values =[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

mainDeck = Deck()

#creating the main deck
for value in values:
    for suit in suits:
        card = Card(suit, value)
        mainDeck.addCard(card)   

mainDeck.shuffle()
playerHand = Hand()

print("-----------------------------")
print("|  Welcome to the game 21!  |")
print("-----------------------------")
print("You will play against a robot!")

#the player is given one card at the start of the game
deckCard = mainDeck.removeCard()
playerHand.takeCard(deckCard)
playerHand.getStatus()

#the player can decide to take cards as long as he is under 21
while playerHand.calculateHandValue() < 21:
    takeMore = input("Would you like to draw? y/n > ")
    if takeMore == "y" or takeMore == "yes" or takeMore == "ja" or takeMore == "k" or takeMore == "ok":
        deckCard = mainDeck.removeCard()
        playerHand.takeCard(deckCard)
        playerHand.getStatus()
    else:
        print("You decide not to draw")
        break
    
if playerHand.calculateHandValue() == 21:
      print("You win! Robot lost!")
      exit()

elif playerHand.calculateHandValue() > 21:
    print("You lost! Robot won!")
    exit()

#robot plays against the player.
#if the points are under 14, he always takes a card
#if the points are 14-16, he makes a random choice
#over 18 - he doesn't take it

robotHand = Hand()

robotHand.takeCard(deckCard)

while robotHand.calculateHandValue() < 14:
      print("It's robot's turn")
      time.sleep(2)
      deckCard = mainDeck.removeCard()
      robotHand.takeCard(deckCard)
      print("Robot takes another card.")
      time.sleep(2)
      robotHand.getStatus()
      time.sleep(2)
while robotHand.calculateHandValue() < 16:
      print("It's robot's turn")
      robotChoice = random.choice(["yes", "no"])
      if robotChoice == "yes":
            print("Robot takes another card.")
            deckCard = mainDeck.removeCard()
            robotHand.takeCard(deckCard)
            time.sleep(2)
            robotHand.getStatus()
      else:
            print("Robot doesn't take another card")
            break

if robotHand.calculateHandValue() > 21:
      print("Robot loses! You win!")
elif robotHand.calculateHandValue() > playerHand.calculateHandValue():
      print("Robot wins!")
elif robotHand.calculateHandValue() < playerHand.calculateHandValue():
      print("You win!")