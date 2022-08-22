from random import shuffle
from Card import *
from operator import itemgetter

class Deck:
    global cards
    global ranks
    global suits
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    

    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
        shuffle(self.cards)
        

    def __repr__(self):
        dictionary = {
            "Hearts": [],
            "Spades": [],
            "Diamonds": [],
            "Clubs": []
        }
        for card in self.cards:
            array = str(card).split(" of ")
            dictionary[array[1]].append(array[0])

        result = ""
        for key in dictionary:
            dictionary[key].sort()
            dictionary[key][0], dictionary[key][9] = dictionary[key][9], dictionary[key][0]
            dictionary[key][11], dictionary[key][12] = dictionary[key][12], dictionary[key][11]
            
            result += f"{key:<8}: "
            for value in dictionary[key]:
                result += value + ", "
                
            result = result[0:-2] + "\n"

        return result
#         print(dictionary["Hearts"][0])
        # deal the deck
    def deal(self):
        return self.cards.pop()



# if __name__ == '__main__':
#     deck = Deck()
#     print(deck.__repr__())