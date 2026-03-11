# if car x is behind the car y, and x need less time to achieve target than y, then x and y will become a fleet
# t = (target-position)/speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True) # 距离终点最近的放在index 0

        stack = []
        for p, s in cars:
            # 计算当前车到达终点的理想时间
            arrival_time = (target-p)/s
            
            # 栈为空，或者当前的车比前车慢，表示追不上，就成了新的领头羊
            if len(stack)==0 or arrival_time>stack[-1]:
                stack.append(arrival_time)
        
        return len(stack)