# def card_val():


# class Deck:

# def __init__(self):

suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

worth = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

deck = {}

def hand_val(hand: dict):
    # for v in hand:
    v_sum = sum(hand.values())
    return v_sum

def blackjack(v_sum: int):
    if v_sum > 21:
        print(f"You busted: {v_sum}")
    if v_sum == 21:
        print(f"Big Winner!!! {v_sum}")
    else:
        pass
#
# def dealer_play(v_sum: int)
#     if v_sum < 15:
#         mv_random_card(comp_hand)


#
# def card_detail():
#     for s in suit:
#         for w in worth:
#             card = {s, worth[w]}
#             deck.update(card)
#             # break
#         # s += 1
#         # w += len(worth)
#         print(deck)


print(deck)


    #     # s <= len(suit[])
    #     x = 0
    #     deck[suit[s]] = worth[x]
    #     deck.update(s)
    #     s += 1
    #     s <= len(suit)
    #     # w += 1
    #     return deck

# print()


def main():
    card_detail()

#
#
#
if __name__ == '__main__':
    main()