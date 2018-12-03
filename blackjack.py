import numpy as np
import random
import math
import matplotlib.pyplot as plt

#Monte(15, 1000000, 8, 2) #turning point, monte times, deck, player)

class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = []

    def __init__(self, deck):
        self.deck = deck
        CardPool.current_pool = CardPool.suit * 4 * self.deck
        random.shuffle(CardPool.current_pool) #建立cardpool实体时即完成洗牌

    def drawCard(self):
        t = self.current_pool.pop(0)
        print(self.current_pool)
        print(len(self.current_pool))
        return t

#class Player:
#    def __init__(self):
#     palyer_sum = 0
#     def __init__(self):
#     def playerDraw(self,):
#         player_sum = drawCard()

def initCard(self):
    pc1 = c.drawCard()  # player明牌
    player_sum = pc1
    if pc1 == 1:
        player_ace = 1
        player_sum += 10
    else:
        player_ace = 0

    dc1 = c.drawCard()  # dealer明牌
    dealer_sum = dc1
    if dc1 == 1:
        dealer_ace = 1
        dealer_sum += 10
    else:
        dealer_ace = 0

    pc2 = c.drawCard()  # player第二张明牌
    player_sum = player_sum + pc2
    if pc2 == 1:
        player_ace += 1
        player_sum += 10

    dc2 = c.drawCard()  # dealer第二张暗牌
    dealer_sum = dealer_sum + dc2
    if dc2 == 1:
        dealer_ace += 1
        dealer_sum += 10

def playerSplit(self):
        if pc2 == 1:
            player_ace -= 1
            player_sum = player_sum - 10

            player_ace_s = 1
            player_sum_s = 11
        else:
            player_sum = player_sum - pc2
            player_ace_s =0
            player_sum_s = pc2

        pc2 = c.drawCard()#给pc1补牌
        if pc2 == 1:
            player_ace += 1
            player_sum += 10
        player_sum += pc2

        p2c2 = c.drawCard() #给分出的牌补牌
        if p2c2 == 1:
            player_ace_s += 1
            player_sum_s += 10
        player_sum_s += p2c2

def if_bust(sum, ace):
    while sum > 21:
        if ace > 0:
            sum = sum - 10
            ace -= 1
        else:
            break
    if sum > 21:
        return -1
    else:
        break

def playerStand(self,standPoint):
def playerHit(self):

def Game(self, nplayer,splitChoice,): #if splitChoice is True, always split if allowed

    c = CardPool(6)
    initCard()

    # 发牌结束，玩家move
    if splitChoice == True:
        if pc1 == pc2:
            playerSplit()
            splitFlag = True
        else:
            break

    while player_sum <= standPoint:
        pc_n = c.drawCard()
        player_sum += pc_n
        if pc_n == 1:
            player_ace += 1
            player_sum += 10

    if_bust(player_sum, player_ace)

    #if splitFlag == True:

    #dealer move
    while delaer_sum < 17:
        dl_n = c.drawCard()
        dealer_sum += pc_n
    if dl_n == 1:
        dealer_ace += 1
        dealer_sum += 10
    if_bust(dealer_sum, dealer_ace)


    #未爆牌玩家与未爆牌的dealer比大小
    if result not in [1,-1]:
        if dealer_sum > player_sum:
            result = -1
        if dealer_sum < player_sum
            result = 1
        if dealer_sum == player_sum
            result = 0

    return result

# def MonteGame(times,standpoint):
#     for i in range(1,times):
#         t = Game(standpoint)
#         i += 1
#