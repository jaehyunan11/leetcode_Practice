class Solution:
    def isRobotBounded(self, instructions):
        # direction 0: North, 1: West, 2: South, 3:East
        # Loop instructions
        # L : dict to 1
        # R : dict to 3
        # G : move direction to 0,1,2,3,
        # bounded condition should be either [0,0]
        # or direction should not be faced to North
        # return pos = [0,0] or direc != 0
        direc = 0
        pos = [0, 0]
        for c in instructions:
            if c == 'L':
                # direc to 1
                direc = (direc+1) % 4
            elif c == 'R':
                # direc to 3
                direc = (direc-1) % 4
            # Go stright to N,S,W,E
            elif c == 'G':
                # 0 as North
                if direc == 0:
                    pos[1] += 1
                # 1 for West
                elif direc == 1:
                    pos[0] -= 1
                # 2 for South
                elif direc == 2:
                    pos[1] -= 1
                else:
                    pos[0] += 1
        return pos == [0, 0] or direc != 0

# TIME : O(N) number of instructions to parse
# Space : O(1) array direction contains only 4 elements


S = Solution()
instructions = "GGLLGG"
print(S.isRobotBounded(instructions))
