import unittest
from mock import Mock
from unittest.mock import patch
# import main_app
import random
from main_app import move_card, mv_random_card, comp_build

class TestBjack(unittest.TestCase):

    def setUp(self) -> None:
        self.deck_dict = {}
        self.ht_dict = {'4 of C': 4}
        self.ht_dict2 = {'A of C': 1}
        self.ht_dict3 = {'2 of C': 2}
        self.ht_dict4 = {'3 of C': 3}

    def test_move_card(self):

        # deck_dict = {}
        #
        # ht_dict = {'4 of C': 4}

        move_card(self.ht_dict, self.deck_dict, '4 of C')
        self.assertDictEqual(self.deck_dict, {'4 of C': 4})
        self.assertDictEqual({}, self.ht_dict)

    def test_mv_random_card(self):
        """unit test for
    def mv_random_card(to_hand: dict):
    random_card = random.choice(list(undealt.keys()))
    move_card(undealt, to_hand, random_card)"""

        # test_dict = {'9 of C': 9,
        #              '6 of C': 6,
        #              '8 of C': 8,
        #              '7 of C': 7,
        #              }
        # ht_dict = {'6 of H': 6, '7 of H': 7, '8 of H': 8, '9 of H': 9, }#

        mv_random_card(self.ht_dict)
        result = '4 of C'
        self.assertEqual(result, random.choice(list(self.ht_dict.keys())))
        self.assertEqual('A of C', random.choice(list(self.ht_dict2.keys())))
        self.assertEqual('2 of C', random.choice(list(self.ht_dict3.keys())))
        self.assertEqual('3 of C', random.choice(list(self.ht_dict4.keys())))


    def test_comp_build(self):
        comp_build(('4 of C': 4))
        self.assertDictEqual()
        # test = {'key': 'value'}
        # original = ht_dict[test].copy()
        # with patch.dict(test, {'9 of C': 9}, clear=True):
        #     assert test == original
        #
        # # result = main_app.move_card(test_dict, ht_dict, card="'9 of C': 9")
        # self.assertEqual(result, ht_dict={)

        # mock = Mock(result=ht_dict[{'9 of C': 9}])
        # try:
        #     mock.assert_called_with(result=ht_dict[{'9 of C': 9}])

        # (from_hand: dict, to_hand: dict, card: str):
        #     to_hand[card] = from_hand.pop(card)





    #
    # for face, value in test_dict:
    #     with self.assertEqual(move_card = )
