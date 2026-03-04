# main_stack = [], min_stack = []
# num = -2: main_stack.append(-2) ==> main_stack = [-2], min_stack=[-2]
# num = -1: main_stack.append(-1) ==> main_stack = [-2, -1], min_stack = [-2]
# num = -3: main_stack.append(-3) ==> main_stack = [-2, -1, -3], min_stack = [-2, -3]
# top: main_stack[-1]=-3
# getMin: min_stack[-1] = -3
# pop: main_stack.pop(), main_stack = [-2, -1]

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None: # time: O(1)
        self.main_stack.append(val)
        if len(self.min_stack)==0 or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None: # time: O(1)
        res = self.main_stack.pop()
        if res==self.min_stack[-1]: # min_stack have to pop element too 
            self.min_stack.pop()
        
    def top(self) -> int: # time: O(1)
        return self.main_stack[-1]

    def getMin(self) -> int: # time: O(1)
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3) 
print(obj.min_stack) # [-2, -3]
print(obj.main_stack) # [-2, 0, -3]

print(obj.getMin()) # -3

obj.pop()
print(obj.main_stack) # [-2, 0]
print(obj.min_stack) # didn't pop the element from the min_stack
print(obj.top()) # 0

print(obj.getMin())
