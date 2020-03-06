class ModeStack:
    def __init__(self):
        self.stack = []
        self.count = {}

    def push(self, value):
        if value not in self.count:
            self.count[value] = 1
        else:
            self.count[value] += 1
        if self.stack:
            mode = self.mode()
            if self.count[mode] < self.count[value]:
                mode = value
        else:
            mode = value
        self.stack.append((value, mode))

    def pop(self):
        value, mode = self.stack.pop()
        self.count[value] -= 1
        return value

    def mode(self):
        if self.stack:
            return self.stack[-1][1]


if __name__ == "__main__":
    stack = ModeStack()
    assert stack.mode() is None
    stack.push(5)
    assert stack.mode() == 5
    stack.push(1)
    assert stack.mode() == 5
    stack.push(1)
    assert stack.mode() == 1
    assert stack.pop() == 1
    assert stack.mode() == 5
    assert stack.pop() == 1
    assert stack.mode() == 5
    assert stack.pop() == 5
    assert stack.mode() is None
