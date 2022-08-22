from Rank import *
from Suit import *


class Card:   
    def __init__(self, value, suit):
        if value not in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            raise ValueError("Invalid value: " + value)
        self.value = Rank(value)
        if suit.lower() not in ["hearts", "spades", "diamonds", "clubs"]:
            raise ValueError("Invalid suit: " + suit)
        self.suit = Suit(suit)
        
        
    def __str__(self):
        return str(self.value)+ " of " + str(self.suit)
    
