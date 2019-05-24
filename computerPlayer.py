from btree import LinkedBinaryTree
from random import choice
from game import Game
from player import Player


class ComputerPlayer(Player):
    """Class for computer player representation"""

    @staticmethod
    def _change_symbol(symbol):
        """
        Extra method for changing symbol
        :param symbol:
        :return:
        """
        if symbol == "O":
            return "X"
        return "O"

    def position_choose(self):
        """
        Choost the position
        :return: position
        """
        tree = LinkedBinaryTree(self.game)
        current_symbol = self.symbol_type
        random_position = self.random_positions(self.game)
        if len(random_position) == 1:
            return random_position[0]
        game_left = Game()
        game_right = Game()
        game_left.set_symbol(random_position[0][0], random_position[0][1], current_symbol)
        if game_left.game_over():
            return self._gameOver_check(current_symbol)

        game_right.set_symbol(random_position[0][0], random_position[0][1], current_symbol)
        if game_right.game_over():
            return self._gameOver_check(current_symbol)

        current_symbol = self._change_symbol(current_symbol)

        def recurse(game, current_symbol):

            if game.draw():
                return 0

            # Create two new Games
            new_game1 = self._new_game(game)
            new_game2 = self._new_game(game)

            # Find two random possible positions
            random_positions = self.random_positions(game)

            new_game1.set_symbol(random_positions[0][0], random_positions[0][1], current_symbol)
            if new_game1.game_over():
                return self._gameOver_check(current_symbol)
            tree.insert_right(new_game1)

            if len(random_positions) == 1:
                current_symbol = self._change_symbol(current_symbol)
                return recurse(new_game1, current_symbol)

            new_game2.set_symbol(random_positions[1][0], random_positions[1][1], current_symbol)
            if new_game2.game_over():
                return self._gameOver_check(current_symbol)

            current_symbol = self._change_symbol(current_symbol)
            tree.insert_left(new_game2)

            return recurse(new_game1, current_symbol) + recurse(new_game2, current_symbol)

        if recurse(game_left, current_symbol) > recurse(game_right, current_symbol):
            return random_position[0]
        return random_position[1]

    def _new_game(self, game):
        """
        Extra method creating new game
        :param game: Game
        :return: Game
        """
        new_game = Game()
        for i in range(3):
            for j in range(3):
                new_game.board.field[i, j] = game.board.field[i, j]
                new_game.board.field[i, j] = game.board.field[i, j]
        new_game.symbol_number = game.symbol_number
        return new_game

    def _gameOver_check(self, current_symbol):
        """
        Extra method
        :param current_symbol: str
        :return: 1 or -1
        """
        if current_symbol == self.symbol_type:
            return 1
        else:
            return -1

    def set_symbol(self):
        """
        Set symbol into position
        :return:
        """
        row, col = self.position_choose()
        self.game.set_symbol(row, col, self.symbol_type)

    def possible_positions(self, game):
        """

        :param game: Game
        :return: number of empty positions
        """
        return game.board.empty_positions()

    def random_positions(self, game):
        """
        number of two random positions
        :param game:
        :return:
        """
        possible_positions = self.possible_positions(game)

        first_position = choice(possible_positions)
        possible_positions.remove(first_position)
        if possible_positions:
            second_position = choice(possible_positions)
        else:
            return [first_position]
        return [first_position, second_position]
