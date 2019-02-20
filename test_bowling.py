import unittest
from bowling import Bowling

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    def test_score(self):
        self.assertEqual(self.game.score(), 0)

if __name__ == '__main__':
    unittest.main()
