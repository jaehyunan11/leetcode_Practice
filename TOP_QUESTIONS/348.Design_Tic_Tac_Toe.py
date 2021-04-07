class TicTacToe:

    def __init__(self, n):
        # size board n
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        # first element is diagonal second element is antodiagonal
        self.diag = [0] * 2

    def move(self, row, col, player):
        # (row, col, player)
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # There are only n (rows) + n (cols) + 2 (diagonals) ways to win the game
        # So use a list or hash table to record the occurance
        # For player 1, +1; for player 2, -1, verify the value after each call to determine the winner

        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            # diagonal case
            if row == col:
                self.diag[0] += 1
            # antidiagonal case
            if row + col == self.n-1:
                self.diag[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.diag[0] == self.n or self.diag[1] == self.n:
                return 1
        # player 2
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diag[0] -= 1
            if row+col == self.n-1:
                self.diag[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.diag[0] == -self.n or self.diag[1] == -self.n:
                return 2
        return 0

        # TIME COMPLEXITY : O(1) ##
        # SPACE COMPLEXITY : O(N) ##


self.row = [0] * 3
row = 1
col = 0
print(row[0])
