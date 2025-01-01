from .__base__ import Sequence
from .node import Node


class Stack(Sequence):
    def __init__(self, size=1000):
        super().__init__()
        self._head = None
        self._max_size = size

    def push(self, value):
        if not self:
            self._head = Node(value)
            self._size = 1
            return

        if len(self) >= self._max_size:
            raise OverflowError("the stack has reached its maximum capacity.")

        self._head = Node(value, self._head)
        self._size += 1

    def pop(self):
        if not self:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self):
        return None if not self else self._head.value

    def clear(self):
        self._size = 0
        self._head = None
