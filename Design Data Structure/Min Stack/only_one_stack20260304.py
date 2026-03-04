class MinStack:
    def __init__(self):
        # stack中存储差值，维护一个min值
        self.stack = []
        self.min = None
        
    def push(self, val: int) -> None: # time: O(1)
    # 每次都将差值推入栈中，并维护更新self.min
        if not self.stack:
            self.min = val 
            diff = val-self.min
            self.stack.append(diff)
        else:
            diff = val-self.min
            self.stack.append(diff)
            if diff<0: # val<self.min：更新min
                self.min = val

    def pop(self) -> None: # time: O(1)
        diff = self.stack.pop()
        if diff<0: # current_min-previous_min=diff<0 ==> previous_min=current_min-diff
            self.min = self.min-diff
        
    def top(self) -> int: # time: O(1)
        diff = self.stack[-1]
        if diff>=0: # value-min>=0==>value>=min==>value=min+diff
            return self.min+diff
        else:  # value<previouw_min ==> value = min 当前元素就是最新的最小值
            return self.min

    def getMin(self) -> int: # time: O(1)
        return self.min
