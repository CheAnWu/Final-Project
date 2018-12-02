import random
import matplotlib.pyplot as plt
import math


Hit = 0
Stick = 1

global results
global total_deck
global total_hands
global split_count
global stick_count
global player_1_card
global player_2_card
global dealer
global bust
global action

split_count = False #判斷是否要split
stick_count = False #判斷是否要stick
bust = False #判斷是否爆掉（超過21點）
player_1_card = [] # player的手牌
player_2_card = [] # 如果要進行split的動作，player的第二副手牌
dealer = [] #dealer的手牌
action = [] #執行的動作




def card_pool():
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    del total_deck[:]
    i = 0
    while i < 2: # 2 decks
        for card in cards:
            total_deck.append(card)
        i += 1
    random.shuffle(total_deck)

def init_draw(self): # 一開始的發牌
    card = [total_deck.pop(0)] #取出第一張牌
    self.append(card[0])

def dealer_draw(self): #dealer一開始的發牌
    card = [total_deck.pop(0)]
    self.append(card[0])

def draw_card(self): #hit之後的發牌
    action.append('Hit')
    self.init_draw(self)

def stick(self):
    global stick_count
    action.append('Stick')
    stick_count = True

def dealer_extra_draw(self):
    while count_score(self) < 17:
        init_draw(self)

def wager(): # 籌碼
    return 1 # 假設一局價值一個籌碼

def split(self):
    global split_count
    split_count = True
    action.append('Split')
    self.pop(1)
    player_2_card.append(self[0])
    self.draw_card(self)
    self.draw_card(player_2_card)

def count_score(self):
    global bust
    global hardtotal
    total = 0
    total_without_ace = True
    ace = 0
    for cards in self:
        if cards == "J" or cards == "Q" or cards == "K":
            total += 10
        elif cards == "A":
            total += 11
            ace += 1
            total_without_ace = False
        else:
            total += cards

    while ace > 0 and total > 21:
        total -= 10
        ace -= 1
    if ace == 0:
        total_without_ace = True
    if total > 21:
        bust = True
    return total

def compare_card(self, dealer):
    if count_score(self) > 21: # player超過21點
        return -1
    elif count_score(self) == 21 and len(self) == 2: #player為21點且只有兩張牌（代表是black jack）
        if count_score(self) == count_score(dealer): #player與dealer同為21點，但是player是blackjack，所以player獲勝
            return 1
        else: # player為blackjack且player獲勝
            return 2
    elif count_score(self) > count_score(dealer):
        return 1
    elif count_score(dealer) > 21:
        return 1
    elif count_score(self) == count_score(dealer):
        return 0
    else:
        return -1

def game_process():
    global results
    global total_deck
    global total_hands # 總共有幾副手牌
    global split_count
    global stick_count
    global player_1_card
    global player_2_card
    global dealer
    global bust
    global action
    global first_hand_bust
    global second_hand_bust

    split_count = False  # 判斷是否要split
    stick_count = False  # 判斷是否要stick
    bust = False  # 判斷是否爆掉（超過21點）
    first_hand_bust = False # 判斷split後的第一副牌是否burst
    second_hand_bust = False # 判斷split後的第二副牌是否burst
    player_1_card = []  # player的手牌
    player_2_card = []  # 如果要進行split的動作，player的第二副手牌
    dealer = []  # dealer的手牌
    action = []  # 執行的動作
    results = []

################################ 開始遊戲 ##################################

    init_draw(player_1_card) #發player第一張牌
    init_draw(player_1_card) #發player第二張牌
    init_draw(dealer) #發dealer第一張牌
    dealer_draw(dealer) #發dealer第二張牌

    while bust == False and stick_count == False:
        if bust == False and stick_count == False:
            round1 = [count_score(player_1_card[:-1]), count_score(dealer[0]), 0, action[-1]]
            results.append(round1)
    if bust == True and stick_count == False:
        round1 = [count_score(player_1_card[:-1]), count_score([dealer[0]]), -1 * wager(), action[-1]]
        results.append(round1)
        first_hand_bust = True
    stick_count = False
    bust = False
    total_hands += 1

    if split_count == True:
        total_hands += 1
    while split_count == True and stick_count == False and bust == False:
        if stick_count == False and bust == False:
            round1 = [count_score(player_2_card[:-1]), count_score([dealer[0]]), 0, action[-1]]
            results.append(round1)
    if split_count == True and stick_count == False and bust == True:
        round1 = [count_score(player_2_card[:-1]), count_score([dealer[0]]), -1 * wager(), action[-1]]
        results.append(round1)
        second_hand_bust = True
    dealer_extra_draw(dealer)
    if first_hand_bust == False:
        score = compare_card(player_1_card, dealer)
        round1 = [count_score(player_1_card[:-1]), count_score([dealer[0]]), score * wager(), action[-1]]
        results.append(round1)
    if second_hand_bust == False and split_count == True:
        score2 = compare_card(player_2_card, dealer)
        round2 = [count_score(player_1_card[:-1]), count_score([dealer[0]]), score * wager(), action[-1]]
        results.append(round2)
