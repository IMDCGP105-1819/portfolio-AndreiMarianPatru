import random
from itertools import islice
#card class used for creating cards objects
class Card():
  def __init__(self, color, suit, rank):
    self.color = color
    self.suit = suit
    self.rank = rank
    #display a card sensibly
  def display(self):
    print( '{2}-{0}-{1}'.format(self.color, self.suit,self.rank))
#deck class whill create a 52 card-objects list
class Deck():
  def __init__(self):

    self.deck=[]
    for i in range(1,15):

      if i != 11:#1 and 11 are the same in a deck
        self.deck.append(Card("red","heart",i))
        self.deck.append(Card("red","diamond",i))
        self.deck.append(Card("black","club",i))
        self.deck.append(Card("black","spade",i))
    #make our deck random
    random.shuffle(self.deck)


#hand class creates hands of 5 cards, taking items from the deck created above
  def get_hand( theDeck ):
    #check if there are enough cards to make a new hand
    l = len(theDeck.deck)
    if l < 5:
      print("No more hands to deal")
    else:
      print("Press e to deal a hand")
      #get the first 5 items from our deck
      iterator = islice(theDeck.deck, 5)
      remain = slice(5,l)
      theDeck.deck = theDeck.deck[remain]
      #show the hand created
      for i in iterator:
        i.display()

#create an instance of a deck
theDeck = Deck()
#make the player able to deal hands
print("Press e to deal a hand")
while True:
    ans=input()
    if ans=="e":
        Hand.get_hand(theDeck)
        print()
