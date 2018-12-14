
import random
class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = []

    def __init__(self, deck):
        self.deck = deck
        CardPool.current_pool = CardPool.suit * 4 * self.deck
        random.shuffle(CardPool.current_pool) #建立cardpool实体时即完成洗牌

    def drawCard(self):
        t = self.current_pool.pop(0)
        print(t)
        #print(self.current_pool)
        #print(len(self.current_pool))
        return t

def initCard(sum,ace):
    card = c.drawCard()  # player明牌
    sum = card + sum
    if card == 1:
        ace += 1
        sum += 10
    else:
        ace += 0
    return (sum,ace,sum)

c = CardPool(6)
sum = 0
ace = 0
print(sum)
print(ace)
t=initCard(sum, ace)
print(t[0],t[1])
t=initCard(sum, ace)
print(t[0],t[1])
