# from bjack_mod import card_detail
# import bjack_test
import random
import numpy as np


comp_hand = {}

player_hand = {}

# player_move = {
#     1: "Hit",
#     2: "Stand",
#     3: "Leave the Game",
# }


def intro():
    kv_ = {
        'Q of H': 10,
        '6 of C': 6,
        '2 of D': 2,
        '7 of S': 7,
        '4 of D': 4,
        'K of H': 10,
    }

    _kv_ = list(kv_.items())
    np.random.shuffle(_kv_)
    kv_ = dict(_kv_)
    c_card = kv_.popitem()
    p_card = kv_.popitem()
    return c_card, p_card


def comp_build(c_card: set):
    comp_hand.update(c_card)
    return comp_hand


def player_build(p_card: set):
    player_hand.update(p_card)
    return player_hand


def hand_val(comp_hand: dict):
    for k, v in comp_hand:
        sum(comp_hand.values(k))
        return sum


def hand_val(player_hand: dict):
    for k, v in player_hand:
        sum(player_hand.values(v))
        return sum


def hands(comp_hand, player_hand):
    print("Welcome to my BlackJack table\n")
    comp_build(comp_hand)
    print(f"Dealer's Hand showing {hand_val(comp_hand)}")
    player_build(player_hand)
    input("")



#
# def dealer(card):
#     for card in deck:
#         comp_hand.update(card)




def main():
    intro()
#
#
#
if __name__ == '__main__':
    main()
