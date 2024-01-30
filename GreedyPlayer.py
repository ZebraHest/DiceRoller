from abc import ABC

from player import Player
import evaluator

class GreedyPlayer(Player, ABC):

    def play(self, game):
        self.player_data.reset_dice()
        roll(self)
        result = evaluator.evaluate(self.player_data.dices, self.player_data.score_sheet)
        self.player_data.add_to_scoresheet(self.player_data.dices, result)

def roll(self):
    self.player_data.roll()
