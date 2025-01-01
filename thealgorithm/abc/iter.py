from ..sorting import quick


class MutSequence:
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return len(self) != 0

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def sort(self, reverse: bool = False):
        quick(self, 0, len(self) - 1, reverse)
