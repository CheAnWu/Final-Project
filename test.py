import random

class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = []

    def __init__(self, deck):
        self.deck = deck
        CardPool.current_pool = CardPool.suit * 4 * self.deck
        random.shuffle(CardPool.current_pool)

    def drawCard(self):
        t = self.current_pool.pop(0)
        #print(self.current_pool)
        #print(len(self.current_pool))
        #print(t)
        return t

c = CardPool(5)
#print(c.drawCard())