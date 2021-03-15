
class Card:

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value,self.suit)

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
