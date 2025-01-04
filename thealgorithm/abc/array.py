from .base import MutSequence
import ctypes


class Array(MutSequence):
    def __init__(self, ctype, size, iterable=None):
        super().__init__(size)
        self.ctype = ctype
        self.array = (ctype * size)()
        self._cptr = 0
        if iterable:
            self.extend(iterable)

    def __setitem__(self, index, value):
        if index == 0:
            self.append(value)
            return
        if index < 0 or index >= self._size or self._cptr <= index:
            raise IndexError("Index out of range.")
        self.array[index] = value

    def __getitem__(self, index):
        if index < 0 or index >= self._size or self._cptr <= index:
            raise IndexError("Index out of range.")
        try:
            value = self.array[index]
            return value
        except ValueError as e:
            if e.args[0] == "PyObject is NULL":
                raise IndexError("Index out of range.") from e
        except Exception:
            raise NotImplemented("Array.__getitem__() is not implemented yet.")

    def __iter__(self):
        for i in range(self._cptr):
            yield self.array[i]

    def extend(self, iterable):
        for value in iterable:
            if self._cptr >= len(self.array):
                raise OverflowError("Array has reached its maximum capacity.")
            self.array[self._cptr] = value
            self._cptr += 1

    def pop(self):
        if self._cptr == 0:
            raise IndexError("pop from empty array")
        value = self.array[self._cptr - 1]
        self.array[self._cptr - 1] = self.ctype()
        self._cptr -= 1
        return value

    def append(self, value):
        if self._cptr >= len(self.array):
            raise OverflowError("Array has reached its maximum capacity.")
        self.array[self._cptr] = value
        self._cptr += 1

    def clear(self):
        for i in range(self._size):
            self.array[i] = self.ctype()
        self._cptr = 0
