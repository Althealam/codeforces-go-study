# if car x is behind the car y, and x need less time to achieve target than y, then x and y will become a fleet
# t = (target-position)/speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # 1. 按照位置从大到小排序（距离终点最近的车在前面）
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0], reverse = True)

        # 2. 遍历
        res = 0
        current_max_time = 0
        for pos, s in cars:
            # 这辆车能够跑完剩下的路程的时间
            arrival_time = (target-pos)/s

            # 当前的这辆车太慢了，永远无法追上前面的那辆车，所以它变成了一个新车队
            if arrival_time>current_max_time:
                res+=1
                current_max_time = arrival_time
            
        return res