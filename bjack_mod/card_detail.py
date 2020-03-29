# def card_val():


# class Deck:

# def __init__(self):

suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

worth = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

deck = {}


def card_detail():
    for s in suit:
        for w in worth:
            card = {s, worth[w]}
            deck.update(card)
            # break
        # s += 1
        # w += len(worth)
        print(deck)


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