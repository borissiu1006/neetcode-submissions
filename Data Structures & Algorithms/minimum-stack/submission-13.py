class MinStack:

    def __init__(self):
        self.s = []
        self.Min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.Min = val
        else:
            self.s.append(val - self.Min)
            if val < self.Min:
                self.Min = val
        
    def pop(self) -> None:
        pop = self.s.pop()
        if pop < 0:
            self.Min = self.Min - pop # add back pop to restore as prev min

        
    def top(self) -> int:
        top = self.s[-1]
        if top > 0:
            return top + self.Min
        else:
            return self.Min
        

    def getMin(self) -> int:
        return self.Min
        
