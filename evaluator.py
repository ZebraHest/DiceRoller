from typing import List

import object_generator


def evaluate(dice_list: List[object_generator.Dice], score_sheet: object_generator.ScoreSheet) -> int:
    if not is_all_unused(dice_list):
        raise Exception("Can only evaluate unused dice.")
    if len(dice_list) == 0:
        raise Exception("Need dice to evaluate.")

    dice_list = sorted(dice_list, key=lambda dice: dice.value)
    score = 0

    if len(dice_list) == 6:
        if is_three_double_present(dice_list):
            set_all_dice_used(dice_list)
            return 500
        if is_staircase(dice_list):
            set_all_dice_used(dice_list)
            return 1500
        if is_double_triple_present(dice_list):
            value_first_triple = get_triple_value(dice_list[0].value)
            value_second_triple = get_triple_value(dice_list[5].value)
            set_all_dice_used(dice_list)
            return value_first_triple + value_second_triple

    triple_data = is_triple_present(dice_list)
    prev_triple_value = prev_triple(score_sheet)
    if (
            triple_data.is_present and
            triple_data.dice_value != prev_triple_value
    ):
        trip_value = get_triple_value(triple_data.dice_value)
        num_of_trip = triple_data.end_loc - triple_data.start_loc - 1
        score += trip_value * num_of_trip
        for i in range(triple_data.start_loc, triple_data.end_loc+1):
            dice_list[i].used = True

    for d in dice_list:
        if d.used:
            continue

        if d.value == prev_triple_value:
            score += get_triple_value(prev_triple_value)
            d.used = True

        elif d.value == 1:
            score += 100
            d.used = True

        elif d.value == 5:
            score += 50
            d.used = True

    used_dice = []
    for d in dice_list:
        if d.used:
            used_dice.append(d)

    #score_sheet.dice_list.append(used_dice)

    return score


def prev_triple(score_sheet: object_generator.ScoreSheet) -> int:
    used_num_of_dice = 0
    for dl in score_sheet.dice_list:
        used_num_of_dice += len(dl)

    if used_num_of_dice > 0 and used_num_of_dice % 6 == 0:
        return 0

    if len(score_sheet.dice_list) > 0:
        dice_list = score_sheet.dice_list[-1]
        triple_data = is_triple_present(dice_list)
        return triple_data.dice_value
    return 0

def set_all_dice_used(dice_list: List[object_generator.Dice]):
    for d in dice_list:
        d.used = True


def is_triple_present(dice_list: List[object_generator.Dice]) -> object_generator.TripleData:
    value = 0
    loc = 0
    counter = 1
    for d in dice_list:
        if d.value == value:
            counter += 1
        else:
            if counter >= 3:
                return object_generator.TripleData(True, value, loc-counter, loc-1)
            value = d.value
            counter = 1
        loc += 1
    if counter >= 3:
        return object_generator.TripleData(True, value, loc - counter, loc - 1)
    return object_generator.TripleData(False)



def is_double_triple_present(dice_list: List[object_generator.Dice]):
    if is_6_and_unused(dice_list):
        return False

    all_different = dice_list[0].value != dice_list[3].value
    first_equal = dice_list[0].value == dice_list[1].value == dice_list[2].value
    last_equal = dice_list[3].value == dice_list[4].value == dice_list[5].value
    return first_equal and last_equal and all_different


def is_three_double_present(dice_list: List[object_generator.Dice]):
    if is_6_and_unused(dice_list):
        return False
    first_equal = dice_list[0].value == dice_list[1].value
    middle_equal = dice_list[2].value == dice_list[3].value
    last_equal = dice_list[4].value == dice_list[5].value

    all_different = (
            dice_list[0].value != dice_list[2].value and
            dice_list[0].value != dice_list[4].value and
            dice_list[2].value != dice_list[4].value
    )

    return first_equal and middle_equal and last_equal and all_different


def is_all_unused(dice_list: List[object_generator.Dice]):
    for d in dice_list:
        if d.used:
            return False
    return True


def is_staircase(dice_list: List[object_generator.Dice]):
    if is_6_and_unused(dice_list):
        return False
    return (
            dice_list[0].value == 1 and
            dice_list[1].value == 2 and
            dice_list[2].value == 3 and
            dice_list[3].value == 4 and
            dice_list[4].value == 5 and
            dice_list[5].value == 6
    )


def is_6_and_unused(dice_list):
    return len(dice_list) != 6 or not is_all_unused(dice_list)


def get_triple_value(dice_value):
    if dice_value == 1:
        return 1000
    return 100 * dice_value
