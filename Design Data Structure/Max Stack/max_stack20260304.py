class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        self.aux_stack = []
    
    def push(self, val): # time: O(1)
        self.main_stack.append(val)
        if len(self.max_stack)==0 or val>=self.max_stack[-1]:
            self.max_stack.append(val)
    
    def pop(self): # time: O(1)
        res = self.main_stack.pop()
        if res==self.max_stack[-1]:
            self.max_stack.pop()
    
    def top(self): # time: O(1)
        return self.main_stack[-1]
    
    def peekMax(self): # time: O(1)
        return self.max_stack[-1]
    
    def popMax(self): # time: O(n)
        current_max = self.peekMax()
        while self.top!=current_max:
            self.aux_stack.append(self.pop())
        self.pop() # remove the maximal value from the main_stack
        while len(self.aux_stack)!=0:
            self.push(self.aux_stack.pop())
        return current_max
