# import unittest
from card_detail import hand_val as hv
# from card_detail import blackjack as bj
import random
import numpy as np
import sys


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


def player_build(p_card: set):
    player_hand.update(p_card)
    return player_hand


def show_status():
    print(f"Dealer's show card ...{next(iter(comp_hand))}\n")
    print(f"Player showing .......{player_hand}\n")


def winner():
    if hv(comp_hand) == hv(player_hand):
        # self.dealer_play(hv(comp_hand))
        print("That's a draw.\n")
        new_round()
    if hv(comp_hand) > hv(player_hand):
        print(f"Dealer's high {hv(comp_hand)} to {hv(player_hand)}... Loser!!!\n")
        new_round()
    elif hv(comp_hand) < hv(player_hand):
        print(f"Dealer's low {hv(comp_hand)} to {hv(player_hand)}... Winner!!!\n")
        new_round()


class Hit:
    pass

    def input_player_action(self):
        """

        :rtype: object
        """
        action = input("[H]it, [S]tand, or [Q]uit \n").upper()
        if action == 'H':
            mv_random_card(player_hand)
            print(f"{player_hand}...And you're holding {hv(player_hand)}\n")
            blackjack(hv(player_hand))
            Hit.input_player_action(self)
        elif action == 'Q':
            print("goodbye")
            sys.exit(0)
        elif action == 'S':
            print(f"...Dealers showing ...{hv(comp_hand)}")
            print(f"...And you're holding {hv(player_hand)}\n")
            Hit.dealer_play(self, hv(comp_hand))

    def dealer_play(self, v_sum: int):
        if v_sum < 15:
            mv_random_card(comp_hand)
            print(f"Dealers showing {hv(comp_hand)}\n")
            Hit.dealer_play(self, hv(comp_hand))
        if v_sum in range(15, 22):
            # print(f"Dealers showing {hv(comp_hand)}")
            winner()
        if v_sum > 21:
            print(f"Dealer busts {hv(comp_hand)}... Winner!!!\n")


def blackjack(v_sum: int):
    if v_sum > 21:
        print(f"You busted:..... {v_sum}\n")
        new_round()
    if v_sum == 21:
        print(f"BlackJack!!!.... {v_sum}\n")
        new_round()
    else:
        pass


def new_round():
    print("Let's play again...\n")
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
    # print(undealt)
    print("\nWELCOME TO THE BLACKJACK TABLE")
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    show_status()
    # print(len(undealt))
    Hit.input_player_action(self)
    new_round()
    print("flag main")
    while True:
        # show_status()
        Hit.input_player_action(self)

    # comp_build(c_card=tuple)
    # c_hand_val(comp_hand)
    # player_build()
    # p_hand_val()
    # hands()


if __name__ == '__main__':
    main()
