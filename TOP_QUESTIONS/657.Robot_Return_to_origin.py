class Solution:
    def judgeCircle(self, moves):
        x = y = 0
        # U : (x, y+1)
        # R : (x+1, y)
        # L : (x-1, y)
        # D : (x, y-1)
        for move in moves:
            if move == "U":
                y += 1
            elif move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "D":
                y -= 1
        return x == y == 0

    def judgeCircle(self, moves)
    return moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D")

# TIME : O(N) N is length of moves
# space : o(1)
