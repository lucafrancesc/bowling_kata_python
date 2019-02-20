import unittest
from bowling import Bowling

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    def test_score(self):
        self.assertEqual(self.game.score(), 0)

    def test_roll(self):
        self.game.roll(4)
        self.assertEqual(self.game.score(), 4)

    def test_gutter_game(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

if __name__ == '__main__':
    unittest.main()
