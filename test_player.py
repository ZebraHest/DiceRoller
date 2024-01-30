from object_generator import PlayerData
from player import Player


class TestPlayer(Player):

    def __init__(self, name, dice_list: list[int]):
        self.player_data = PlayerData(name)
        self.dice_list = dice_list

    def roll(self):
        data = self.player_data
        for d in data.dices:
            if not d.used:
                d.value = self.dice_list.pop(0)
        data.sort_dice()

    def is_decider_roll_again(self, current_roll_score, last_triple, my_score, opponent_score, remaining_dices):
        return True
