import unittest
import object_generator as gen
import evaluator
import game
from player import Player
from test_player import TestPlayer


class MyTestCase(unittest.TestCase):
    def test_triple(self):
        person = gen.PlayerData("test")
        set_dice(person.dices, [4, 2, 4, 4, 5, 4])
        person.sort_dice()
        triple_data = evaluator.is_triple_present(person.dices)
        assert triple_data.is_present
        assert triple_data.dice_value == 4
        assert triple_data.start_loc == 1
        assert triple_data.end_loc == 4
        assert not evaluator.is_double_triple_present(person.dices)
        assert not evaluator.is_three_double_present(person.dices)

        set_dice(person.dices, [4, 2, 2, 4, 2, 4])
        person.sort_dice()
        assert evaluator.is_triple_present(person.dices)
        assert evaluator.is_double_triple_present(person.dices)
        assert not evaluator.is_three_double_present(person.dices)

        set_dice(person.dices, [4, 2, 1, 1, 2, 4])
        person.sort_dice()
        assert not evaluator.is_triple_present(person.dices).is_present
        assert not evaluator.is_double_triple_present(person.dices)
        assert evaluator.is_three_double_present(person.dices)

        person.dices[2].used = True
        set_dice(person.dices, [4, 2, 4, 2, 2, 4])
        person.sort_dice()
        assert evaluator.is_triple_present(person.dices).is_present
        assert not evaluator.is_double_triple_present(person.dices)
        assert not evaluator.is_three_double_present(person.dices)


    def test_play(self):
        person = gen.PlayerData("test")

        set_dice(person.dices, [4, 2, 5, 2, 5, 4])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 500

        person.reset()
        set_dice(person.dices, [4, 1, 3, 2, 6, 5])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 1500

        person.reset()
        set_dice(person.dices, [4, 4, 4, 1, 1, 1])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 1400

        person.reset()
        set_dice(person.dices, [4, 4, 4, 4, 2, 2])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 800

        dice_list = set_and_create_dice([4, 2])
        assert evaluator.evaluate(dice_list, person.score_sheet) == 400

        person.reset()
        set_dice(person.dices, [1, 1, 1, 1, 1, 1])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 4000

        person.reset()
        set_dice(person.dices, [4, 1, 1, 5, 6, 2])
        assert evaluator.evaluate(person.dices, person.score_sheet) == 250


    def test_player_1(self):
        player1 = TestPlayer('player 1', [1,1,1,2,3,4,1,5,3,3,4,4])
        player1.play(0)

    def test_player_2(self):
        player1 = TestPlayer('player 2', [1,1,1,1,5,5, 1,2,3,3,4,4, 3,4,6,2,3, 4,6,2,3,4,6])
        player1.play(0)

    def test_player_3(self):
        player1 = TestPlayer('player 3', [1,1,1,2,5,5, 1, 2,2,2,4,4,5, 1,4,6,2,3,4, 6,2,3,4,6])
        player1.play(0)




def set_and_create_dice(dice_values):
    list = []
    for i in range(len(dice_values)):
        list.append(gen.Dice())
    set_dice(list, dice_values)
    return list


def set_dice(dice_list, dice_values):
    for i in range(len(dice_values)):
        dice_list[i].value = dice_values[i]

def retset(person):
    for i in range(6):
        person.dices[i].used = False



if __name__ == '__main__':
    unittest.main()
