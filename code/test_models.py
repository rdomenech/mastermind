import unittest

from models.game import GameModel


class TestGetResult(unittest.TestCase):

    def test_none_pegs(self):

        game = GameModel()
        game.first = 'black'
        game.second = 'black'
        game.third = 'black'
        game.fourth = 'black'

        result = game.get_result(['white', 'white', 'white', 'white'])
        self.assertEqual(result, (0, 0), 'None pegs should be expected')

    def test_one_white_peg(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'black'
        game.third = 'black'
        game.fourth = 'black'

        result = game.get_result(['green', 'white', 'white', 'white'])
        self.assertEqual(result, (0, 1), 'One white peg should be expected')

    def test_two_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'black'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['green', 'white', 'white', 'green'])
        self.assertEqual(result, (0, 2), 'Two white pegs should be expected')

    def test_three_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'yellow'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['yellow', 'white', 'white', 'green'])
        self.assertEqual(result, (0, 3), 'Three white pegs should be expected')

    def test_four_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'yellow'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['yellow', 'white', 'white', 'black'])
        self.assertEqual(result, (0, 4), 'Four white pegs should be expected')

    def test_one_black_peg(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'yellow'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'blue', 'blue'])
        self.assertEqual(result, (1, 0), 'One black peg should be expected')

    def test_two_black_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'blue', 'blue'])
        self.assertEqual(result, (2, 0), 'Two black pegs should be expected')

    def test_three_black_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'black', 'blue'])
        self.assertEqual(result, (3, 0), 'Three black pegs should be expected')

    def test_four_black_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'black', 'white'])
        self.assertEqual(result, (4, 0), 'Four black pegs should be expected')

    def test_one_black_one_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'green', 'blue', 'yellow'])
        self.assertEqual(result, (1, 1), 'One black and one white pegs should'
                                         ' be expected')

    def test_one_black_two_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'white', 'blue', 'yellow'])
        self.assertEqual(result, (1, 2), 'One black and two white pegs should'
                                         ' be expected')

    def test_one_black_three_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'white', 'blue', 'black'])
        self.assertEqual(result, (1, 3), 'One black and three white pegs '
                                         'should be expected')

    def test_two_black_one_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'blue', 'black'])
        self.assertEqual(result, (2, 1), 'Two black and one white pegs should'
                                         ' be expected')

    def test_two_black_two_white_pegs(self):

        game = GameModel()
        game.first = 'white'
        game.second = 'blue'
        game.third = 'black'
        game.fourth = 'white'

        result = game.get_result(['white', 'blue', 'white', 'black'])
        self.assertEqual(result, (2, 2), 'Two black and two white pegs should '
                                         'be expected')


if __name__ == '__main__':
    unittest.main()
