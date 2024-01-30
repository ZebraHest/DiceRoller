from typing import Tuple, Optional, Union, List

import gymnasium as gym
from gym import Env
from gym.core import ActType, ObsType, RenderFrame
from gym.spaces import MultiBinary, MultiDiscrete
import numpy as np
import random

from player import Player





class EnvV1(Env):
    def __init__(self):
        self.action_space = MultiBinary(7)
        self.observation_space = MultiDiscrete([7, 7, 7, 7, 7, 7, 7, 10000, 10000])
        self.score = 0
        self.current_roll = 0
        self.player = Player("player1")
        self.player.roll()

    def step(self, action: ActType) -> Tuple[ObsType, float, bool, bool, dict]:
        print(action, self.player.player_data.dices)
        roll_again = action[0]
        action = action[1:]
        if not any(action) \
                or not self.is_usable_dice(action)\
                or self.score > 10000\
                or 10000 > self.score > 9750:
            print(self.score)
            return [], -100000, True, {}


        current_roll_score, remaining_dices, result = self.player.handle_dice_action(0, 0, action)

        print(self.score, current_roll_score, result)

        if not roll_again:
            self.score += current_roll_score
            self.current_roll = 0
            self.player.player_data.reset_dice()

        self.player.roll()
        dice_list = self.player.get_dice_as_int(self.player.player_data.dices)
        score = self.score
        last_triple = self.player.get_prev_triple()

        dice_list.append(score)
        dice_list.append(last_triple)
        dice_list.append(self.current_roll)

        done = score == 10000

        return dice_list, result, done, {}

    def render(self) -> Optional[Union[RenderFrame, List[RenderFrame]]]:
        pass

    def reset(
            self,
            *,
            seed: Optional[int] = None,
            options: Optional[dict] = None,
    ) -> Tuple[ObsType, dict]:
        self.player.player_data.reset()
        self.player.roll()
        self.score = 0
        self.current_roll = 0


        dice_list = self.player.get_dice_as_int(self.player.player_data.dices)
        score = 0
        last_triple = 0
        current_roll_score = 0

        dice_list.append(score)
        dice_list.append(last_triple)
        dice_list.append(current_roll_score)

        return dice_list

    def is_usable_dice(self, action):
        for i in range(len(action)):
            if action[i] and not self.player.player_data.dices[i].used:
                return True
        return False

