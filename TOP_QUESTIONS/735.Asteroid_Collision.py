class Solution:
    def asteroidCollision(self, asteroid):
        # positive -> right
        # negative <- left
        # absolute value represents its size
        # if two asteroids meet, smller asteroids is exploded
        # both are same size, both asteroids are exploded.
        # two asteroids moving in the same direction will never meet
        res = []

        for x in asteroid:
            # Inside the while loop there will be a colission.
            # negative in asteroid vs postive in res
            while len(res) and x < 0 and res[-1] > 0:
                # sum of two asteroid are zero then pop asteroid in res
                if (res[-1]) + x) == 0:
                    res.pop()
                    break
                elif abs(x) < res[-1]:
                    break
                else:
                    res.pop()
                    continue
            else:
                res.append(x)
        return res
# TIME : o(N)
# space : o(N)
S=Solution()
