# if car x is behind the car y, and x need less time to achieve target than y, then x and y will become a fleet
# t = (target-position)/speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0]) # 第一个元素距离终点最远

        time = [] # 按照position从小到大排序（time[0]是马路上最后面的车，time[1]是马路上最前面的车，距离终点最近）
        for i in range(n):
            time.append((target-cars[i][0])/cars[i][1])

        stack = []  # 存储的是所有可能成为独立车队的领头羊的时间
        for i in range(len(time)):
            # 栈底是整条路上最靠后、并且时间最长的那个慢车
            # 栈顶是目前为止发现的距离终点最近的那个车队的时间
            while len(stack)!=0 and time[i]>=stack[-1]:  # time[i]是位置更靠前的车，stack[-1]是位置更靠后的车，当前车i的时间>=后车的时间时，表示前车比后车慢，因此后车会和前车组成一个车队
                stack.pop()
            stack.append(time[i])
        return len(stack)