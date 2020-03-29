import unittest
from mock import Mock
from unittest.mock import patch
import main_app

class TestBjack(unittest.TestCase):

    def test_move_card(self):
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




    #
    # for face, value in test_dict:
    #     with self.assertEqual(move_card = )
