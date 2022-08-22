from Card import *
from Deck import *
from Player import *
   
    
p1 = Player()
p1.name = input("Please enter your name: ")
p2 = Player()
p2.name = input("Please enter your name: ")
deck = Deck()
while len(deck.cards) > 0:
    p1_card = deck.deal()
    print(p1_card)
    p2_card = deck.deal()
    print(p2_card)
    if p1_card.value > p2_card.value:
        p1.wins = p1.wins + 1
        print(p1.name + " wins!")
    elif p1_card.value < p2_card.value:
        p2.wins = p2.wins + 1
        print(p2.name + " wins!")
    elif p1_card.value == p2_card.value:
        p1_card = deck.deal()
        p2_card = deck.deal()
        print(p1_card)
        print(p2_card)
        p1_card = deck.deal()
        p2_card = deck.deal()
        print(p1_card)
        print(p2_card)
print(p1.name + ":" + str(p1.wins))
print(p2.name + ":" + str(p2.wins))
if p1.wins > p2.wins:
    print(p1.name + " won War!")
elif p2.wins > p1.wins:
    print(p2.name + " won War!")
elif p1.wins == p2.wins:
    print("It's a tie!")