class Solution:
    def isRobotBounded(self, instructions):
        # inital stands (0,0) faces to north
        # "G" go straight 1 unit
        # "L" turn 90 degress to the left
        # "R" turn 90 degress to the right

        # 4 directions (North, West, South, East)
        # 0 : North, 1: West, 2: South, 3:East

        direc = 0
        # start points
        pos = [0, 0]

        # loop the instructions
        for c in instructions:
            if c == "L":
                # face to counter clock wise (e.g. direc = 0, 1 % 4 = 1)
                direc = (direc+1) % 4
                # face to clock wise (e.g. direc = 0, -1 % 4 = 3)
            elif c == "R":
                direc = (direc-1) % 4
            elif c == "G":
                # go to north
                if direc == 0:
                    pos[1] += 1
                elif direc == 1:
                    pos[0] -= 1
                elif direc == 2:
                    pos[1] -= 1
                else:
                    pos[0] += 1
        # pos is 0,0 or robot doesn't face to north side then it is true
        return pos == [0, 0] or direc != 0

# TIME : O(N) n is number of instructions to parse
# Space : O(1) since there are array contains only 4 directions


S = Solution()
instructions = "GG"
print(S.isRobotBounded(instructions))
