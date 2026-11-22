class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []
        res = []
        for i in range(len(position)):
            position_speed.append([position[i], speed[i]])

        for p,s in sorted(position_speed, reverse=True):

            res.append((target - p) / s)
            if len(res)>=2 and res[-2] >= res[-1]:
                res.pop()
        return len(res)
        