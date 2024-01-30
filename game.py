from GreedyPlayer import GreedyPlayer
from player import Player

score_goal = 10000


def play_new_game():
    player1 = Player('player 1')
    player2 = Player('player 2')

    while score_not_over(player1, player2):
        player1.play()
       # player2.play(player1.get_score())

        print(player1.player_data)
      #  print(player2.player_data)



def score_not_over(player1: Player, player2: Player):
    return not (player1.get_score() >= score_goal or player2.get_score() >= score_goal)
