import random


class Dice:
    def __init__(self):
        self.value = random.randrange(1, 7)
        self.used = False

    def __repr__(self):
        return f"[{self.value}, {self.used}]"

    def roll(self) -> int:
        self.value = random.randrange(1, 7)
        return self.value


class PlayerData:
    def __init__(self, name):
        self.name = name
        self.score_sheet = ScoreSheet()
        self.score = 0
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice(), Dice()]
        self.sort_dice()

    def __repr__(self):
        return f"[{self.name}, {self.get_score()}, {self.dices}]"

    def roll(self):
        for d in self.dices:
            if not d.used:
                d.roll()
        self.sort_dice()

    def print(self):
        print("Player", self.name)
        print("Score", self.score_sheet)
        print(self.dices)

    def sort_dice(self):
        self.dices = sorted(self.dices, key=lambda dice: dice.value)

    def add_to_scoresheet(self, dices, score):
        self.score_sheet.add_score(dices, score)

    def add_score(self, score):
        self.score += score

    def get_score(self) -> int:
        return self.score

    def get_unused_dice(self):
        dice_list = []
        for d in self.dices:
            if not d.used:
                dice_list.append(d)
        return dice_list

    def reset_dice(self):
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice(), Dice()]
        self.sort_dice()

    def reset(self):
        self.score_sheet = ScoreSheet()
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice(), Dice()]
        self.sort_dice()


class ScoreSheet:
    def __init__(self):
        self.score_list = [0]
        self.dice_list = [[]]

    def add_score(self, dices, score):
        self.score_list.append(score)
        self.dice_list.append(dices)

    def get_score(self):
        return sum(self.score_list)


class DiceCup:
    def __init__(self, dices):
        self.dices = dices


class TripleData:
    def __init__(self, is_present, dice_value=0, start_loc=0, end_loc=0):
        self.is_present = is_present
        self.dice_value = dice_value
        self.start_loc = start_loc
        self.end_loc = end_loc
