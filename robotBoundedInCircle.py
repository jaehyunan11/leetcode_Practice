# class Solution:
#     def

# if after the set of operations, the robot is still at the position (0,0) then it is bounded
# if the robot doesn't point North after the set of instuctions, it will
# return to the point (0,0) after 4 sets of instructions, pointing North, and repeat
# Therefore, if the robot doesn't point North after the set of operations, it is bounded.
# IN all other cases, the robot is unbounded

class Solution:
    def isRobotBounded(self, instructions):
        # initial direction
        direc = [0, 0]
        # set pos to 0
        pos = 0
        for c in instructions:
            if c == "L":
                direc = (direc + 1) % 4
            elif c == "R":
                direc = (direc - 1) % 4
            elif c == "G":
                # 0 as North
                if direc == 0:
                    pos[1] += 1
                # 1 as West
                elif direc == 1:
                    pos[0] -= 1
                # 2 as South
                elif direc == 2:
                    pos[1] -= 1
                # 3 as East
                else:
                    pos[0] += 1
        # bounded condition should be either [0,0] or direc is not north.
        return pos == [0, 0] or direc != 0


# class Solution:
#     def isRobotBounded(self, instructions):
#         # robot is bounded if end position is 0,0
#         # OR
#         # end direction is not north
#         n = {'l': 'w', 'r': 'e'}
#         s = {'l': 'e', 'r': 'w'}
#         e = {'l': 'n', 'r': 's'}
#         w = {'l': 's', 'r': 'n'}

#         state = 'n'
#         pos = (0, 0)
#         for i in range(len(instructions)):
#             if instructions[i] == 'G':
#                 if state == 'n':
#                     pos = pos[0], pos[1] + 1
#                 elif state == 's':
#                     pos = pos[0], pos[1] - 1
#                 elif state == 'w':
#                     pos = pos[0] + 1, pos[1]
#                 else:
#                     pos = pos[0] - 1, pos[1]

#             elif instructions[i] == 'L':
#                 if state == 'n':
#                     state = n['l']
#                 elif state == 's':
#                     state = s['l']
#                 elif state == 'w':
#                     state = w['l']
#                 else:
#                     state = e['l']

#             else:
#                 if state == 'n':
#                     state = n['r']
#                 elif state == 's':
#                     state = s['r']
#                 elif state == 'w':
#                     state = w['r']
#                 else:
#                     state = e['r']
#             # print(pos, state)
#             # if state is facing to north is is unbounded.
#             if pos == (0, 0) or state != 'n':
#                 return True
#             return False


class Solution:
    def isRobotBounded(self, instructions):
        direc, pos = 0, [0, 0]
        for c in instructions:
            if c == "L":
                direc = (direc + 1) % 4
            elif c == "R":
                direc = (direc - 1) % 4
            elif c == "G":
                if direc == 0:
                    pos[1] += 1
                elif direc == 1:
                    pos[0] -= 1
                elif direc == 2:
                    pos[1] -= 1
                else:
                    pos[0] += 1
        return pos == [0, 0] or direc != 0


s = Solution()
instructions = "GGLLGG"
print(s.isRobotBounded(instructions))
