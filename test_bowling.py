import unittest
from bowling import Bowling

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    # Gutter game scores zero
    # When you roll all misses, you get a total score of zero.
    def test_gutter_game(self):
        for i in range(23):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    # All ones scores 20
    # When you knock down one pin with each ball, your total score is 20
    def test_1_pin_each_roll(self):
        for i in range(23):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 20)

    # A spare in the first frame, followed by three pins,
    # followed by all misses scores 16
    def test_score_a_spare(self):
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(3)
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 16)

    # A strike in the first frame, followed by three and then four pins,
    # followed by all misses, scores 24
    def test_score_a_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 24)

    # 3 strikes followed by all misses, scores 60
    def test_score_3_strike(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        for i in range(18):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 60)

    # 3 strikes followed by all misses, scores 60
    def test_score_2_strike(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        for i in range(18):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 55)

    # 1 spare, 1 strikes, 1 spare, 1 meh followed by all misses, scores 60
    def test_score_mixed(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(0)
        for i in range(16):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 60)

    # A perfect game (12 strikes) scores 300
    def test_score_a_perfect_game(self):
        for i in range(12):
            self.game.roll(10)
        self.assertEqual(self.game.score(), 300)

    # Almost perfect game (10 strikes) scores 270
    def test_score_a_perfect_game(self):
        for i in range(10):
            self.game.roll(10)
        self.game.roll(0)
        self.game.roll(0)
        self.assertEqual(self.game.score(), 270)

# # print(self.game._frames)
if __name__ == '__main__':
    unittest.main()
