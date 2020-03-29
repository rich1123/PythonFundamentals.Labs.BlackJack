import unittest
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

        result = main_app.move_card(test_dict, ht_dict, card= "'9 of C': 9")
        self.assertEqual(result, ht_dict[card]= test_dict.)

    #
    # for face, value in test_dict:
    #     with self.assertEqual(move_card = )
