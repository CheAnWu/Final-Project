import random
import numpy as np
import pandas as pd
#import math
#import matplotlib.pyplot as plt

class CardPool:
    suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    current_pool = []

    def __init__(self, deck):
        self.deck = deck
        CardPool.current_pool = CardPool.suit * 4 * self.deck
        random.shuffle(CardPool.current_pool)   #Shuffle the cards instantly after created the card pool

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

    @property
    def dealershow(self):
        return self._dealershow
    @dealershow.setter
    def dealershow(self, value):
        if not isinstance(value, int):
            raise ValueError('dealershow must be an int!')
        self._dealershow = value

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
        self.playerhand_split = 0.0

    @property
    def playerhand(self):
        return self._playerhand
    @playerhand.setter
    def playerhand(self, value):
        if not isinstance(value, int):
            raise ValueError('playerhand must be an int!')
        self._playerhand = value
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
        if sum ==12 and ace == 1:
            sum = 11
            ace = 1
        else:
            sum = sum/2
            if ace == 2:
                ace = 1
            else:
                ace = 0
        return (sum, ace)

    @property
    def bust(self):
        return self._bust
    @bust.setter
    def bust(self, value):
        if not isinstance(value, int):
            raise ValueError('bust flag must be int!')
        self._bust = value

    @property
    def bust_s(self):
        return self._bust_s
    @bust_s.setter
    def bust_s(self, value):
        if not isinstance(value, int):
            raise ValueError('bust flag must be int!')
        self._bust_s = value

def if_bust(sum, ace):
    """
    :param sum: Player currently sum of cards in their hand
    :param ace: Player currently numbers of "A" cards in their hand
    :return: return (-1, current number of "A" card) if bust; return (currently sum of players' card, current number of "A" card) if not bust
    >>> if_bust(22, 0)
    (-1, 0)
    >>> if_bust(25, 1)
    (15, 0)
    >>> if_bust(14, 1)
    (14, 1)
    >>> if_bust(16, 0)
    (16, 0)

    """
    while sum > 21:
        if ace > 0:
            sum = sum - 10
            ace -= 1
        else:
            break
    if sum > 21:
        return (-1, ace)
    else:
        return (sum, ace)

def turn(player_sum, dealer_sum):
    """
    :param player_sum: Currently sum of Players' cards
    :param dealer_sum: Currently sum of Dealer's cards
    :return: return 1 if player sum bigger than dealer sum; return 0 if player and dealer sum is tied; return -1 if player sum smaller than dealer sum
    >>> turn(21, 10)
    1
    >>> turn(18, 18)
    0
    >>> turn(15, 21)
    -1
    """
    # if player_sum == 21:
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
    #print('p1',p1.player_sum)

    current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace)
    dealer.dealer_sum = current_score[0]
    dealer.dealer_ace = current_score[1]

    dealer.dealershow = current_score[0]
    #print('d1',dealer.dealer_sum)

    current_score = c.initCard(p1.player_sum, p1.player_ace)
    if current_score[0] - p1.player_sum == p1.player_sum: # Evaluate players' two cards to see if they are the same, if they are the same, then player had a chance to split
        p1.playerhand_split = p1.player_sum
        if splitChoice == True:
            p1.splitflag = True
        # elif current_score[0] == 22:
        #         p1.splitflag = True
        else:
            p1.splitflag = False
            #print('p2', current_score[0] - p1.player_sum)
    else:
        p1.splitflag = False
        #print('p2', current_score[0] - p1.player_sum)
    p1.player_sum = current_score[0]
    p1.player_ace = current_score[1]
    p1.playerhand = current_score[0] #####
    m = if_bust(p1.player_sum,p1.player_ace)
    p1.player_sum = m[0]
    p1.player_ace = m[1]

    current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace) # Dealer's second card
    #print('d2', current_score[0] - dealer.dealer_sum)
    dealer.dealer_sum = current_score[0]
    dealer.dealer_ace = current_score[1]

    if p1.splitflag == True: # Players splits their cards after dealer draw the card

        current_score = p1.playerSplit(p1.player_sum, p1.player_ace)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1] # The first hand after splitting

        p1.player_sum_s = current_score[0]
        #print('ps1', p1.player_sum_s)
        p1.player_ace_s = current_score[1]  # The second hand after splitting

        current_score = c.initCard(p1.player_sum, p1.player_ace)
        #print('p2', current_score[0] - p1.player_sum)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1]  # Draw the second card for the first hand

        current_score = c.initCard(p1.player_sum_s, p1.player_ace_s)
        #print('ps2', current_score[0] - p1.player_sum_s)
        p1.player_sum_s = current_score[0]
        p1.player_ace_s = current_score[1]  # Draw the second card for the second hand

    ######################
    # Finish drawing cards, if the player's current sum of cards if smaller than the standpoint, then hit, if it's bigger, then stand

    while p1.player_sum < p1.standPoint:
        current_score = c.initCard(p1.player_sum,p1.player_ace)
        #print('pn', current_score[0] - p1.player_sum)
        p1.player_sum = current_score[0]
        p1.player_ace = current_score[1]

        r = if_bust(p1.player_sum, p1.player_ace)
        if r[0] == -1: # Player bust
            p1.bust = -1
            break
        else:
            p1.player_sum = r[0]
            p1.player_ace = r[1]

    if p1.splitflag == True:
        while p1.player_sum_s < p1.standPoint:
            current_score = c.initCard(p1.player_sum_s, p1.player_ace_s)
            #print('psn', current_score[0] - p1.player_sum_s)
            p1.player_sum_s = current_score[0]
            p1.player_ace_s = current_score[1]

            r = if_bust(p1.player_sum_s, p1.player_ace_s)
            if r[0] == -1:  # Player bust
                p1.bust_s = -1
                break
            else:
                p1.player_sum_s = r[0]
                p1.player_ace_s = r[1]

    #dealer's move
    if ((p1.bust == -1) and (p1.splitflag == False)): # No split, player bust, end of the game
        #print('Player no split, bust')
        return dealer.dealershow, -1, p1.playerhand, p1.splitflag, p1.playerhand_split

    elif((p1.bust_s ==-1) and (p1.bust == -1)): # Bust in both hands, end of the game
        #print('Both hands of player bust')
        return dealer.dealershow, -2, p1.playerhand, p1.splitflag, p1.playerhand_split

    else: # At least one hand survive(one hand bust or either two hands didn't bust)
        while dealer.dealer_sum < 17:
            current_score = c.initCard(dealer.dealer_sum, dealer.dealer_ace)
            #print('dn', current_score[0] - dealer.dealer_sum)

            dealer.dealer_sum = current_score[0]
            dealer.dealer_ace = current_score[1]
            r = if_bust(dealer.dealer_sum, dealer.dealer_ace)
            if r[0] == -1:  # Dealer bust
                if p1.splitflag == False:
                    #print('Dealer bust, player no bust, no split')
                    return dealer.dealershow, 1, p1.playerhand, p1.splitflag, p1.playerhand_split
                elif ((p1.bust!=-1) and (p1.bust_s!= -1)):
                    #print('Dealer bust, both hands of player no bust')
                    return dealer.dealershow, 2, p1.playerhand, p1.splitflag, p1.playerhand_split
                else:
                    #print('Dealer bust, player one hand win, one hand bust')
                    return dealer.dealershow, 1, p1.playerhand, p1.splitflag, p1.playerhand_split
            else:
                dealer.dealer_sum = r[0]
                dealer.dealer_ace = r[1]

    # At least one hand of player didn't bust and dealer didn't bust too.
    # At the same time, dealer's sum of card is bigger than 17 points, so the dealer no need to draw an extra card.
    # Then compare the cards sum of dealer and player to return the game result

    if p1.splitflag == True:
        if ((p1.bust!=-1) and (p1.bust_s!= -1)):
            result = turn(p1.player_sum, dealer.dealer_sum)
            result = result + turn(p1.player_sum_s, dealer.dealer_sum)
            #print('Split, both player and dealer no bust',result)
        elif ((p1.bust==-1) and (p1.bust_s!= -1)):
            result = turn(p1.player_sum_s, dealer.dealer_sum)
            #print('first hand bust, second hand no bust, dealer no bust', result)
        elif ((p1.bust!=-1) and (p1.bust_s== -1)):
            result = turn(p1.player_sum, dealer.dealer_sum)
            #print('second hand bust, first hand no bust, dealer no bust', result)
    else:
        result = turn(p1.player_sum, dealer.dealer_sum)
        #print('No split, both hands no bust',result)
    return dealer.dealershow, result, p1.playerhand, p1.splitflag, p1.playerhand_split


# sum = 0
# for i in range(10000):
#     r = Game(True,deck=6,standpoint=21)
#     sum = sum + r[1]
#     # if r[1] >= 0:
#     #     sum = sum + 1
#
# print(sum/10000)

# for i in range(1,1000):
#     r = Game(True,6,14)
#     print(r,i)
#     sum = sum + r

"""
for a in range(2, 12):
    count = df[df['Dealer Show'] == a].shape[0]
    dealer_sum = df.loc[df['Dealer Show'] == a, 'Game Result'].sum()
    print('Dealer Show:', a,'Expectation:',dealer_sum/count)
"""
def print_to_file():  # function to feed all the values to a dataframesum = 0
    dealer_show = []
    game_result = []
    player_hand = []
    split_flag = []
    player_split = []
    for i in range(1, 100):
        r = Game(True, deck=6, standpoint=21)
        dealer_show.append(r[0])
        game_result.append(r[1])
        player_hand.append(r[2])
        split_flag.append(r[3])
        player_split.append(r[4])
        #sum = sum + r[1]
    # generating the dataframe with the appropriate column names
    d = {'Dealer Show': dealer_show, 'Game Result': game_result, 'Player Hand': player_hand,
         'Player Hand Split': player_split, 'split flag': split_flag}
    df = pd.DataFrame(d)
    # generating the output csv file
    df.to_csv('BlackJackSimulation21_.csv')

print_to_file()