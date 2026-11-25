class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append((value, value))
        else:
            current_min = self.stack[-1][1]
            new_min = min(current_min, value)
            self.stack.append((value, new_min))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]
