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


def hands(c_card, p_card):
    print("Welcome to my BlackJack table\n")
    comp_build(c_card)
    print(f"Dealer's Hand showing {hand_val(comp_hand)}")
    player_build(p_card)
    input("")


def hand_val(d: dict):
    for v in d:
        sum(d.values())
        return sum
#
# def dealer(card):
#     for card in deck:
#         comp_hand.update(card)

def comp_build(c_card: set):
    comp_hand.update((c_card))
    return comp_hand

def player_build(p_card: set):
    player_hand.update((p_card))
    return player_hand

def main():
    # comp_build()
    # player_build()
    intro()


if __name__ == '__main__':
    main()
