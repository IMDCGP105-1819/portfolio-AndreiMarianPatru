import random

class Card:
    def __init__(self,colour,type,number):
        self.colour=colour
        self.type=type
        self.number=number
class Deck(Card):
    def __init__(self,deck):
        self.deck=deck
    def get_cards(self):
        deck=[]
        for i in range(1,15):
            deck.append(Card("red","heart",i))
            deck.append(Card("red","diamond",i))
            deck.append(Card("black","club",i))
            deck.append(Card("black","spade",i))
        random.shuffle(deck)
        for i in deck:
            if i.number==11:
                deck.remove(i)
        return deck
class Hand(Deck):
    def __init__(self,deck):
        self.deck=deck
    deckCopy=deck
    random.shuffle(deckCopy)
    def get_hand():
        Hand=[]
        counter=1
        for i in deckCopy:
            Hand.append(i)
            deckCopy.remove(i)
            if counter==5:
                break
        return Hand



myDeck=Deck()
MyCards=myDeck.get_cards()
#for x in MyCards:
#    print(x.number," ",x.colour," ",x.type)
myHand=Hand()
randvar=myHand.get_hand()
for x in randvar:
    print(x.number," ",x.colour," ",x.type)
