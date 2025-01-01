from ..sorting import quick


class Sequence:
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

    def __contains__(self, value):
        return self.find(value) >= 0

    def find(self, value):
        raise NotImplementedError("find() method is not implemented yet")


class MutSequence(Sequence):
    def __init__(self):
        super().__init__()

    def sort(self, reverse: bool = False):
        quick(self, 0, len(self) - 1, reverse)
