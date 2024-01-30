import unittest
import game as game


class MyTestCase(unittest.TestCase):
    def test_game(self):
        game.play_new_game()


if __name__ == '__main__':
    unittest.main()
