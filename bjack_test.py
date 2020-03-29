import unittest
from mock import Mock
from unittest.mock import patch
import main_app
import random

class TestBjack(unittest.TestCase):

    def test_move_card(self):
        """unit test for
    def move_card(from_hand: dict, to_hand: dict, card:str):
    to_hand[card] = from_hand.pop(card)"""
        # def __name__
        test_dict = \
        {'9 of C': 9,
                 '6 of C': 6,
                 '8 of C': 8,
                 '7 of C': 7,
                 }

        ht_dict = {}

        test = {'key': 'value'}
        original = ht_dict[test].copy()
        with patch.dict(test, {'9 of C': 9}, clear=True):
            assert test == original

        # result = main_app.move_card(test_dict, ht_dict, card="'9 of C': 9")
        # self.assertEqual(result, ht_dict={)

        # mock = Mock(result=ht_dict[{'9 of C': 9}])
        # try:
        #     mock.assert_called_with(result=ht_dict[{'9 of C': 9}])

        # (from_hand: dict, to_hand: dict, card: str):
        #     to_hand[card] = from_hand.pop(card)

    def test_mv_random_card(self):
        """unit test for
    def mv_random_card(to_hand: dict):
    random_card = random.choice(list(undealt.keys()))
    move_card(undealt, to_hand, random_card)"""

        test_dict = {'9 of C': 9,
                     '6 of C': 6,
                     '8 of C': 8,
                     '7 of C': 7,
                     }
        ht_dict = {'6 of H': 6, '7 of H': 7, '8 of H': 8, '9 of H': 9,}

        result = main_app.mv_random_card(ht_dict)
        self.assertEqual(result, random.choice(list(test_dict.keys())))
    #
    # for face, value in test_dict:
    #     with self.assertEqual(move_card = )
