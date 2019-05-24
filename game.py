from board import Board


class Game:
    """Class for game representation"""
    def __init__(self):
        self.board = Board()
        self.players = []
        self._current_playerIndex = 0
        self._current_player = None
        self.last_added = None
        self.last_coordinates = None, None
        self.symbol_number = 0

    def change_player(self):
        """
        Change current player
        :return:
        """
        if self._current_playerIndex < len(self.players) - 1:
            self._current_playerIndex += 1
        else:
            self._current_playerIndex = 0
        self._current_player = self.players[self._current_playerIndex]

    def game_over(self):
        """
        check if game is over
        :return:  bool
        """
        if self.last_added is None:
            return False

        positions = self.potential_positions(self.last_coordinates[0], self.last_coordinates[1])

        for position in positions:
            if self.board.field[position[0][0], position[0][1]] == self.last_added and \
               self.board.field[position[1][0], position[1][1]] == self.last_added:
                return True
        return False

    def draw(self):
        """
        Check if it is draw
        :return: bool
        """
        return self.symbol_number == 9

    def potential_positions(self, row, col):
        """

        :param row: int
        :param col: int
        :return: return positions that can end game
        """
        return list(filter(lambda x: len(x) == 2, [list(filter(lambda x: 0 <= x[0] <= 2 and 0 <= x[1] <= 2,
                                                               [(row - 2, col),
                                                                (row - 1, col),
                                                                (row + 1, col),
                                                                (row + 2, col)])),
                                                   list(filter(lambda x: 0 <= x[0] <= 2 and 0 <= x[1] <= 2,
                                                               [(row - 1, col + 1),
                                                                (row + 1, col - 1),
                                                                (row + 2, col - 2),
                                                                (row - 2, col + 2)])),
                                                   list(filter(lambda x: 0 <= x[0] <= 2 and 0 <= x[1] <= 2,
                                                               [(row, col - 2),
                                                                (row, col - 1),
                                                                (row, col + 1),
                                                                (row, col + 2)])),
                                                   list(filter(lambda x: 0 <= x[0] <= 2 and 0 <= x[1] <= 2,
                                                               [(row + 1, col + 1),
                                                                (row - 1, col - 1),
                                                                (row + 2, col + 2),
                                                                (row - 2, col - 2)]))]))

    def set_symbol(self, row, col, symbol):
        """
        Set symbol into current position
        :param row: int
        :param col: int
        :param symbol: X or O
        :return:
        """
        self.board.set_symbol(row, col, symbol)
        self.last_added = self.board.field[row, col]
        self.last_coordinates = row, col
        self.symbol_number += 1

    def current_player(self):
        """

        :return: current player
        """
        return self._current_player

    def add_player(self, player):
        """
        Add player
        :param player: Player
        :return:
        """
        self.players.append(player)
        if not self._current_player:
            self._current_player = self.players[0]

    def __str__(self):
        """

        :return: view of board
        """
        return str(self.board)
