import unittest
from bowling import Bowling

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    def test_score(self):
        self.assertEqual(self.game.score(), 0)

    # Gutter game scores zero
    # When you roll all misses, you get a total score of zero.
    def test_gutter_game(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    # All ones scores 20
    # When you knock down one pin with each ball, your total score is 20
    def test_1_pin_each_roll(self):
        for i in range(20):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 20)

    # A spare in the first frame, followed by three pins,
    # followed by all misses scores 16


    # A strike in the first frame, followed by three and then four pins,
    # followed by all misses, scores 24


    # A perfect game (12 strikes) scores 300


if __name__ == '__main__':
    unittest.main()
