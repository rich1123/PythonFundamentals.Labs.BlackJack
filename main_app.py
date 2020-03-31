# import unittest
from card_detail import hand_val as hv
# from card_detail import blackjack as bj
import random
import numpy as np
import sys

# player_move = {
#     1: "Hit",
#     2: "Stand",
#     3: "Leave the Game",
# }


comp_hand = {}

player_hand = {}

undealt = {}
# deck build
for suit in 'H', 'S', 'D', 'C':
    for face, value in [('A', 1), ('2', 2), ('3', 3), ('4', 4),
                        ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                        ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]:
        name = (f"{face} of {suit}")
        undealt[name] = value


def move_card(from_hand: dict, to_hand: dict, card: str):
    to_hand[card] = from_hand.pop(card)


def mv_random_card(to_hand: dict):
    random_card = random.choice(list(undealt.keys()))
    move_card(undealt, to_hand, random_card)


def comp_build(c_card: set):
    comp_hand.update(c_card)
    return comp_hand


# def c_hand_val(comp_hand: dict):
#     # for k, v in comp_hand:
#     c_sum = sum(comp_hand.values())
#     return c_sum


def player_build(p_card: set):
    player_hand.update(p_card)
    return player_hand


# def p_hand_val(player_hand: dict):
#     # for k, v in player_hand:
#     p_sum = sum(player_hand.values())
#     return p_sum

#
# def hands(c_sum, p_sum):
#     print("Welcome to my BlackJack table\n")
#     comp_build(c_sum)
#     print(f"Dealer's show card is {next(iter(c_sum))}")
#     player_build(p_sum)
#     print(f"Player showing {p_sum}")


#
# def dealer(card):
#     for card in deck:
#         comp_hand.update(card)
#
def show_status():
    print(f"Dealer's show card {next(iter(comp_hand))}")
    print(f"Player showing {player_hand}")


class Hit:
    pass

    # def __init__(self):
    # pass
    # action = self.action
    # self.action = input("[H]it, [S]tand, or [Q]uit ").upper()

    # def card_action(self):
    #     return self.action
    # def blackjack(self, v_sum: int):
    #
    #     if v_sum > 21:
    #         print(f"You busted: {v_sum}")
    #         new_round()
    #     if v_sum == 21:
    #         print(f"BlackJack!!! {v_sum}")
    #         new_round()
    #     else:
    #         pass

    def input_player_action(self):
        """

        :rtype: object
        """
        action = input("[H]it, [S]tand, or [Q]uit ").upper()
        if action == 'H':
            mv_random_card(player_hand)
            print(f"{player_hand}...And you're holding {hv(player_hand)}")
            blackjack(hv(player_hand))
            Hit.input_player_action(self)
        elif action == 'Q':
            print("goodbye")
            sys.exit(0)
        elif action == 'S':
            print(f"Dealers showing {hv(comp_hand)}")
            print(f"...And you're holding {hv(player_hand)}")
            Hit.dealer_play(self, hv(comp_hand))

    def dealer_play(self, v_sum: int):
        if v_sum < 15:
            print(f"Dealers showing {hv(comp_hand)}")
            self.dealer_play(v_sum)
        if v_sum in range(15, 22):
            # print(f"Dealers showing {hv(comp_hand)}")
            self.winner()
        if v_sum > 21:
            print(f"Dealer busts {hv(comp_hand)}... Winner!!!")


    def winner(self):
        if hv(comp_hand) == hv(player_hand):
            Hit.dealer_play(hv(self, hv(comp_hand)
       elif hv(comp_hand) > hv(player_hand):
           print(f"Dealer's high {hv(comp_hand)} to {hv(player_hand)}... Loser!!!")
           new_round()
       elif hv(comp_hand) < hv(player_hand):
           print(f"Dealer's low {hv(comp_hand)} to {hv(player_hand)}... Winner!!!")
           new_round()


# def test():


def blackjack(v_sum: int):
    if v_sum > 21:
        print(f"You busted: {v_sum}")
        new_round()
    if v_sum == 21:
        print(f"BlackJack!!! {v_sum}")
        new_round()
    else:
        pass


def new_round():
    print("Let's play again...")
    undeal_cards(player_hand)
    undeal_cards(comp_hand)
    mv_random_card(player_hand)
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    mv_random_card(comp_hand)
    show_status()


def undeal_cards(hand: dict):
    cards = list(hand.keys())
    for card in cards:
        move_card(hand, undealt, card)


def main(self=None):
    print(undealt)
    print("Welcome to the blackjack table")
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    show_status()
    print(len(undealt))
    Hit.input_player_action(self)
    new_round()
    while True:
        show_status()
        Hit.input_player_action(self)

    # comp_build(c_card=tuple)
    # c_hand_val(comp_hand)
    # player_build()
    # p_hand_val()
    # hands()


if __name__ == '__main__':
    main()
