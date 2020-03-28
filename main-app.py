import card_detail
import bjack_test

comp_hand = {}

player_hand = {}

player_move = {
    1: "Hit",
    2: "Stand",
    3: "Leave the Game",
}


def intro():
    print("Welcome to my BlackJack table\n")
    print(f"Dealer's Hand showing {hand_val(comp_hand)}")
    input("")

def hand_val(d: dict):
    for v in d:
        sum(d.values())
        return sum

def comp_build():


def player_build():


def main():
    intro()


if __name__ == '__main__':
    main()
