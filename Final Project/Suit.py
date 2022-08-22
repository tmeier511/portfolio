class Suit(object):
    _suit = None

    def __init__(self, suit):
        if suit.lower() not in ["hearts", "spades", "diamonds", "clubs"]:
            raise ValueError("Invalid suit: " + suit)
        self._suit = suit

    def __str__(self):
        return self._suit


