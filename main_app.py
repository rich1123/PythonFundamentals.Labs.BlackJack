# import unittest
import bjack_test
import random
import numpy as np


# player_move = {
#     1: "Hit",
#     2: "Stand",
#     3: "Leave the Game",
# }


comp_hand = {}

player_hand = {}

undealt = {}
# deck build
for suit in 'H', 'Q', 'D', 'C':
    for face, value in [('A', 1), ('2', 2), ('3', 3), ('4', 4),
                        ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                        ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]:
        name = (f"{face} of {suit}")
        undealt[name] = value

def move_card(from_hand: dict, to_hand: dict, card:str):
    to_hand[card] = from_hand.pop(card)

def mv_random_card(to_hand: dict):
    random_card = random.choice(list(undealt.keys()))
    move_card(undealt, to_hand, random_card)


# def intro():
#     undealt_ = list(undealt.items())
    # np.random.shuffle(undealt)
    # undealt = dict(undealt_)
    # c_card = kv_.popitem()
    # p_card = kv_.popitem()
    # return c_card, p_card


def comp_build(c_card: set):
    comp_hand.update(c_card)
    return comp_hand


def c_hand_val(comp_hand: dict):
    # for k, v in comp_hand:
    c_sum = sum(comp_hand.values())
    return c_sum


def player_build(p_card: set):
    player_hand.update(p_card)
    return player_hand


def p_hand_val(player_hand: dict):
    # for k, v in player_hand:
    p_sum = sum(player_hand.values())
    return p_sum


def hands(c_sum, p_sum):
    print("Welcome to my BlackJack table\n")
    comp_build(c_sum)
    print(f"Dealer's Hand showing {c_sum}")
    player_build(p_sum)
    print(f"Player showing {p_sum}")


#
# def dealer(card):
#     for card in deck:
#         comp_hand.update(card)

def show_status():
    print(f"Dealer's Hand showing {comp_hand}")
    print(f"Player showing {player_hand}")

def input_player_action():
    action = input("[H]it, [S]tand, or [Q]uit ").upper()
    if action == 'H':
        mv_random_card(player_hand)

def new_round():
    undeal_cards( player_hand)
    undeal_cards(comp_hand)
    mv_random_card(player_hand)
    mv_random_card(player_hand)
    mv_random_card(comp_hand)
    mv_random_card(comp_hand)

def undeal_cards(hand: dict):
    cards = list(hand.keys())
    for card in cards:
        move_card(hand, undealt, card)


def main():
    # intro()
    # build_deck()
    print(undealt)
    mv_random_card(player_hand)
    mv_random_card(player_hand)
    print(player_hand)
    print(p_hand_val(player_hand))
    print(len(undealt))
    new_round()
    while True:
        show_status()
        input_player_action()

    # comp_build(c_card=tuple)
    # c_hand_val(comp_hand)
    # player_build()
    # p_hand_val()
    # hands()


if __name__ == '__main__':
    main()
