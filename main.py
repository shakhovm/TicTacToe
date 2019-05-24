# The process of game

from computerPlayer import ComputerPlayer
from game import Game
from player import Player

game = Game()

game.add_player(Player(input("Enter name: "), "X", game))

checker = input("Do you wanna play with computer? (Yes or Not)")
while True:
    if checker == "Yes":
        game.add_player(ComputerPlayer("Tic-toc-toe-player #1", "O", game))
        break
    elif checker == "No":
        game.add_player(Player(input("Enter name: "), "O", game))
        break
    else:
        print("Please enter yes or no")


while True:
    print("---------------")
    print(game)
    print("---------------")
    if game.game_over():
        print("Winner is {}".format(cur_player))
        break
    if game.draw():
        print("Draw")
        break

    cur_player = game.current_player()
    if isinstance(cur_player, ComputerPlayer):
        cur_player.set_symbol()
    else:
        while True:
            try:
                cur_player.set_symbol(int(input("Input row: ")), int(input("Input col: ")))
                break
            except IndexError:
                print("Please, enter row and col within 0, 2 and to the empty position")
    game.change_player()

