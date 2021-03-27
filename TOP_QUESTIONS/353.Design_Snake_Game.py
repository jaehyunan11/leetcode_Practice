class SnakeGame:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food
        self.positions = [[0, 0]]  # initializing queue at [0,0]
        self.score = 0

    def move(self, directions):
        # compute the new head
        head = self.positions[0]

        # direction of head
        if directions == 'U':
            newHead = [head[0]-1, head[1]]
        elif directions == 'D':
            newHead = [head[0]+1, head[1]]
        elif directions == 'L':
            newHead = [head[0], head[1]-1]
        elif directions == 'R':
            newHead = [head[0], head[1]+1]

        if self.positions and newHead in self.positions:
            if self.positions[-1] != newHead:
                return -1

        # if newHead is out of boundary or in the boundard
        if newHead[0] == -1 or newHead[0] == self.height or newHead[1] == -1 or newHead[-1] == self.width:
            return -1

        self.positions.insert(0, newHead)

        if self.food and newHead == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            # if food not found then the length of snake didn't increase and hence tail will move forward
            self.positions.pop()
        return self.score
