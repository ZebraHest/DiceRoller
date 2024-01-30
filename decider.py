import random


class Decider:
    def dice_to_use(self, dices: list[int], my_score: int, last_triple: int,
                    current_roll_score: int) -> list[bool]:
        list = []
        rand = random.Random()
        list.append(rand.randint(0, 100) < 50)
        for i in range(len(dices)):
            list.append(True)

        return list

    # def roll_again(self, dices_left: int, my_score: int, opponent_score: int, last_triple: int,
    #               current_roll_score: int) -> bool:
    #    rand = random.Random()
    #    return rand.randint(0, 100) < 50
