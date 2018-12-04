import numpy as np
import random
import math
import matplotlib.pyplot as plt

#Monte(15, 1000000, 8, 2) #stand point, monte times, deck, player)

class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = []

    def __init__(self, deck):
        self.deck = deck
        CardPool.current_pool = CardPool.suit * 4 * self.deck
        random.shuffle(CardPool.current_pool)   #建立cardpool实体时即完成洗牌

    def drawCard(self):
        t = self.current_pool.pop(0)
        #print(self.current_pool)
        #print(len(self.current_pool))
        return t

    def initCard(self, sum, ace):
        card = self.drawCard()
        sum = card + sum
        if card == 1:
            ace += 1
            sum += 10
        else:
            ace += 0
        return (sum, ace)

class Dealer:
    def __init__(self):
        self.dealer_sum = 0
        self.dealer_ace = 0

class Player:
    def __init__(self,standPoint):
        self.standPoint = standPoint
        self.player_sum = 0
        self.player_ace = 0

        self.player_sum_s = 0
        self.player_ace_s = 0

        self.bust = 0
        self.bust_s = 0
        self.splitflag = False

    # @property
    # def split_ace(self):
    #     return self._split_ace
    # @split_ace.setter
    # def split_ace(self, value):
    #     if not isinstance(value, bool):
    #         raise ValueError('split ace must be an bool!')
    #     self._split_ace = value

    @property
    def splitflag(self):
        return self._splitflag
    @splitflag.setter
    def splitflag(self, value):
        if not isinstance(value, bool):
            raise ValueError('split flag must be an bool!')
        self._splitflag = value

    def playerSplit(self, sum, ace):
        sum = sum/2
        if ace == 2:
            ace = 1
        else:
            ace = 0
        return (sum, ace)

    @property
    def bust(self):
        return self._bust
    @splitflag.setter
    def bust(self, value):
        if not isinstance(value, int):
            raise ValueError('bust flag must be int!')
        self._bust = value

    @property
    def bust_s(self):
        return self._bust
    @splitflag.setter
    def bust_s(self, value):
        if not isinstance(value, int):
            raise ValueError('bust flag must be int!')
        self._bust = value

def if_bust(sum, ace):
    while sum > 21:
        if ace > 0:
            sum = sum - 10
            ace -= 1
        else:
            break
    if sum > 21:
        return (-1,ace)
    else:
        return (sum,ace)

def turn(player_sum, dealer_sum):
    # if player_sum == 21:
    #    return
    if player_sum > dealer_sum:
        r = 1
    elif player_sum == dealer_sum:
        r = 0
    elif player_sum < dealer_sum:
        r = -1
    return r


def Game(splitChoice, deck, standpoint): #nplayer #if splitChoice is True, always split if allowed

    c = CardPool(deck)
    p1 = Player(standpoint)
    dealer = Dealer()

    current_score = c.initCard(p1.player_sum, p1.player_ace)
    p1.player_sum = current_score[0]
    p1.player_ace = current_score[1]

    current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace)
    dealer.dealer_sum = current_score[0]
    dealer.dealer_ace = current_score[1]

    current_score = c.initCard(p1.player_sum, p1.player_ace)
    if current_score[0] - p1.player_sum == p1.player_sum: #判断两张牌是否相等及是否要分牌
        if splitChoice == True:
            p1.splitflag = True
            # if p1.player_ace == 1:
            #     p1.split_ace = True
            # else:
            #     p1.split_ace = False
        else:
            p1.splitflag = False
    p1.player_sum = current_score[0]
    p1.player_ace = current_score[1]

    current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace) #dealer暗牌
    dealer.dealer_sum = current_score[0]
    dealer.dealer_ace = current_score[1]

    if p1.splitflag == True: #分牌在庄家发完暗牌之后
        current_score = p1.playerSplit(p1.player_sum, p1.player_ace)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1] #分牌后的牌A

        p1.player_sum_s = current_score[0]
        p1.player_ace_s = current_score[1]  #分牌后的牌B

        current_score = c.initCard(p1.player_sum, p1.player_ace)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1]  #牌A补牌

        current_score = c.initCard(p1.player_sum_s, p1.player_ace_s)
        p1.player_sum_s = current_score[0]
        p1.player_ace_s = current_score[1]  #牌B补牌

    ######################
    #发牌结束，玩家move;要牌或爆牌

    while p1.player_sum < p1.standPoint:
        current_score = c.initCard(p1.player_sum,p1.player_ace)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1]

        r = if_bust(p1.player_sum, p1.player_ace)
        if r[0] == -1: #玩家爆牌
            p1.bust = -1
            break
        else:
            p1.player_sum = r[0]
            p1.player_ace = r[1]

    if p1.player_sum_s != 0:
        while p1.player_sum_s < p1.standPoint:
            current_score = c.initCard(p1.player_sum_s, p1.player_ace_s)
            p1.player_sum_s = current_score[0]
            p1.player_ace_s = current_score[1]

            r = if_bust(p1.player_sum_s, p1.player_ace_s)
            if r[0] == -1:  # 玩家爆牌
                p1.bust_s = -1
                break
            else:
                p1.player_sum_s = r[0]
                p1.player_ace_s = r[1]

    #dealer's move
    if p1.bust_s ==-1 and p1.bust == -1 : #两手牌均爆，游戏结束
        return -2
    elif p1.bust == -1 and p1.splitflag == False : #未split，爆牌，游戏结束
        return -1
    else:
        while dealer.dealer_sum < 17:
            current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace)
            dealer.dealer_sum = current_score[0]
            dealer.dealer_ace = current_score[1]
            r = if_bust(dealer.dealer_sum, dealer.dealer_ace)
            if r[0] == -1:  # 庄家爆牌
                if p1.splitflag == False:
                    return 1
                elif (p1.bust!=-1) and (p1.bust_s!= -1):
                    return 2
                else:
                    return 1
            else:
                dealer.dealer_sum = r[0]
                dealer.dealer_ace = r[1]

    #玩家、庄家均未爆牌且庄家牌超过17，比较结果
    if p1.splitflag == True:
        result = turn(p1.player_sum, dealer.dealer_sum)
        result = result + turn(p1.player_sum_s, dealer.dealer_sum)
    else:
        result = turn(p1.player_sum, dealer.dealer_sum)

    return result

print(Game(True,6,14))

########
# def MonteGame(times,standpoint):
#     for i in range(1,times):
#         t = Game(standpoint)
#         i += 1