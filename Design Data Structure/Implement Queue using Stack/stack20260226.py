# stack_in: 1 2 3 (out)
# stack_out: 3 2 1 stack_in: NULL 
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.remove_if_empty()
        return self.stack_out.pop()
        
    def peek(self) -> int:
        self.remove_if_empty()
        return self.stack_out[-1]

    def empty(self) -> bool:
        if len(self.stack_in)==0 and len(self.stack_out)==0:
            return True
        return False
    
    def remove_if_empty(self):
        if len(self.stack_out)==0:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())


        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()