import random
#card class used for creating cards objects
class Card:
    def __init__(self,colour,type,number):
        self.colour=colour
        self.type=type
        self.number=number
#deck class whill create a 52 card-objects list
class Deck():
    def __init__(self):
        pass
    deck=[]
    for i in range(1,15):
        deck.append(Card("red","heart",i))
        deck.append(Card("red","diamond",i))
        deck.append(Card("black","club",i))
        deck.append(Card("black","spade",i))
    random.shuffle(deck)
    #removing cards with number 11 because 1 and 11 cards are the same
    for i in deck:
        if i.number==11:
            deck.remove(i)
#hand class creates hands of 5 cards, taking items from the list created in deck class
class Hand():
    def __init__(self):
        pass

    def get_hand():
        copydeck=Deck.deck[:]
        random.shuffle(copydeck)
        counter=1
        #show the hands created using an empty line after each hand
        for i in copydeck:
            print('{} {} {}'.format(i.number,i.type,i.colour))
            if counter==5:
                print()
                counter=0
            counter+=1

        print("No more cards to deal")


Hand.get_hand()
