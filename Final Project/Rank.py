class Rank(object):
    global ranks
    _rank = None
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank):
        if rank not in ranks:
            raise ValueError("Invalid rank: " + rank)
        self._rank = rank

    def __str__(self):
        return self._rank

    def __gt__(self, p2):
        if self.value > p2.value:
            return True
        else:
            return False
        
    def __lt__(self, p2):
        if self.value < p2.value:
            return True
        else:
            return False
    
    def __eq__(self, p2):
        if self.value == p2.value:
            return True
        else:
            return False
        
    @property
    def value(self):
        value_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
        return int(value_dict[self._rank])
        
# if __name__ == "__main__":
#     rank = Rank("3")
#     print(rank)
#     rank = Rank("A")
#     print(rank)