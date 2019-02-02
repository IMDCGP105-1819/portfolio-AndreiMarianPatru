import random

class Card:
    def __init__(self,colour,type,number):
        self.colour=colour
        self.type=type
        self.number=number
class Deck(Card):
    def __init__(self):
        pass
    def get_cards(self):
        deck=[]
        for i in range(1,15):
            deck.append(Card("red","heart",i))
            deck.append(Card("red","diamond",i))
            deck.append(Card("black","club",i))
            deck.append(Card("black","spade",i))
        for i in deck:
            if i.number==11:
                deck.remove(i)
        return deck
a=Deck()
b=a.get_cards()
for x in b:
    print(x.number," ",x.colour," ",x.type)
