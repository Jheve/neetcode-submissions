class MinStack:

    def __init__(self):
        # stor cur minimum in stack
        self.min = float('inf')

        # store encoded vals instead of nums
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val  - self.min)

            # update cur minimum
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        popped = self.stack.pop()

        # if popped element is negative -> element was minimum
        if popped < 0:
            self.min = self.min - popped
        
    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.min
        else:
            return self.min        
        
    def getMin(self) -> int:
        return self.min
        
