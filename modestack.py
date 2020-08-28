from typing import Dict, List, Tuple


class ModeStack:
    def __init__(self) -> None:
        self.stack: List[Tuple[int, int]] = []
        self.count: Dict[int, int] = {}

    def push(self, value: int) -> None:
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

    def pop(self) -> int:
        value = self.stack.pop()[0]
        self.count[value] -= 1
        return value

    def mode(self) -> int:
        return self.stack[-1][1]
