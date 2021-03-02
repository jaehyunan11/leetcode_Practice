class TicTacToe:
    def __init__(self, n):
        # TIME Complexity : O(1)
        # Space Complexity : O(N)
        # There are only n(rows) + n(cols) + 2 (diagonals) ways to win the game
        # So, use a list or hash table to recordd the occurance
        # For player1, +1; for player 2, -1 verify the value after each call to determine the winner
        self.n = n
        self.rows = [0] * n  # total sums by row
        self.cols = [0] * n  # total sums by column
        self.dias = [0] * 2

    def move
