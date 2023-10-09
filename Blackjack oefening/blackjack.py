import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#computer_draw = random.choice(cards)
# print(computer_draw)

play_blackjack = input('Do you want to play a game of blackjack, "y" or "n"?')
#pc_cards = [random.choice(cards),random.choice(cards)]
#user_cards = [random.choice(cards),random.choice(cards)]

def play(play_blackjack):
    if play_blackjack == 'y':
        pc_cards = [random.choice(cards), random.choice(cards)]
        user_cards = [random.choice(cards), random.choice(cards)]
        print(pc_cards,user_cards)
        if sum(pc_cards) >21 or sum(user_cards) >21:
            cards[11] = cards[1]


play(play_blackjack)