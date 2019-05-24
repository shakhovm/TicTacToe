class Player:
    """CLass for player representation"""
    def __init__(self, name, symbol_type, game):

        if symbol_type != 'X' and symbol_type != 'O':
            raise ValueError
        self.name = name
        self.symbol_type = symbol_type
        self.symbols_positions = []
        self.game = game

    def set_symbol(self, row, col):
        """
        Set symbol in certain position
        :param row: int
        :param col: int
        :return:
        """
        if row < 0 or row > 2 or col < 0 or col > 2 or not self.game.board.is_empty(row, col):
            raise IndexError
        self.symbols_positions.append((row, col))
        self.game.set_symbol(row, col, self.symbol_type)

    def __str__(self):
        """

        :return: name of player
        """
        return self.name
