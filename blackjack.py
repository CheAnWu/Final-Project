import numpy as np
import random
import math
import matplotlib.pyplot as plt

#Monte(15, 1000000, 8, 2) #turning point, monte times, deck, player)

class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = suit * 4 * deck

    def drawCard(self):
        t = random.choice(self.current_pool)
        current_pool = current_pool - t
        return t

def Game(self, standpoint, split):
    player_sum = drawCard() #player明牌
    dealer_sum = drawCard() #dealer明牌
    if dealer_sum == 1:
        dealer_ace = True
    else:
        pass
    player_sum = player_sum + drawCard() #player第二张明牌
    dealer_sum = dealer_sum + drawCard() #dealer第二张暗牌

    #if dealer_ace == True:
        #insurance

    #不考虑split，玩家move
    while player_sum <= standpoint:
        player_sum = drawCard()
        if player_sum > 21:
            result = -1
            break
        else:
            continue

    #dealer move
    if result == -1:
        break
    else:
        while dealer_sum <= 17:
            dealer_sum = drawCard()
            if dealer_sum > 21:
                result = 1
                break
            else:
                continue

    if result not in [1,-1]:
        if dealer_sum > player_sum:
            result = -1
        if dealer_sum < player_sum
            result = 1
        if dealer_sum == player_sum
            result = 0

    return result