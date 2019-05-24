from arrays import Array2D


class Board:
    """Class for board representation"""
    def __init__(self):
        self.field = Array2D(3, 3)
        for i in range(self.field.num_rows()):
            for j in range(self.field.num_cols()):
                self.field[i, j] = '-'

    def set_symbol(self, row, col, symbol):
        """
        Set symbol into current position
        :param row: int
        :param col: int
        :param symbol: X or O
        :return:
        """
        self.field[row, col] = symbol

    def is_zero(self, row, col):
        """

        :param row: int
        :param col: int
        :return: bool
        """
        return self.field[row, col] == 'X'

    def is_cross(self, row, col):
        """
        Check if certain position is cross
        :param row: int
        :param col: int
        :return: bool
        """
        return self.field[row, col] == 'O'

    def is_empty(self, row, col):
        """
        Check if certain position is empty
        :param row: int
        :param col: int
        :return: bool
        """
        return self.field[row, col] == '-'

    def empty_positions(self):
        """

        :return: number of empty positions
        """
        positions = []
        for i in range(self.field.num_rows()):
            for j in range(self.field.num_cols()):
                if self.is_empty(i, j):
                    positions.append((i, j))
        return positions

    def __str__(self):
        """

        :return: view of board
        """
        field = ""
        for i in range(self.field.num_rows()):
            field += "|"
            for j in range(self.field.num_cols()):
                field += str(self.field[i, j])
            field += '|\n'
        return field
