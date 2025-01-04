import ctypes
import unittest

from thealgorithm.abc import array
from thealgorithm.abc.number import icomplex


class TestArray(unittest.TestCase):

    def test_array_with_ints(self):
        arr = array(ctype=ctypes.c_int, size=5, iterable=[1, 2, 3])
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)

    def test_array_with_strings(self):
        arr = array(ctype=ctypes.c_wchar_p, size=3, iterable=["hello", "world"])
        self.assertEqual(arr[0], "hello")
        self.assertEqual(arr[1], "world")

    def test_array_set_item_strings(self):
        arr = array(ctype=ctypes.c_wchar_p, size=3)
        arr[0] = "test"
        self.assertEqual(arr[0], "test")

    def test_array_with_complex_numbers(self):
        arr = array(ctype=icomplex, size=4, iterable=[icomplex(1, 2), icomplex(3, 4)])
        self.assertEqual(arr[0], icomplex(1, 2))
        self.assertEqual(arr[1], icomplex(3, 4))

    def test_array_set_item_complex(self):
        arr = array(ctype=icomplex, size=2)
        arr[0] = icomplex(5, 6)
        self.assertEqual(arr[0], icomplex(5, 6))

    def test_array_with_frozenset(self):
        arr = array(
            ctype=ctypes.py_object,
            size=3,
            iterable=[frozenset({1, 2}), frozenset({3, 4})],
        )
        self.assertEqual(arr[0], frozenset({1, 2}))
        self.assertEqual(arr[1], frozenset({3, 4}))
        with self.assertRaises(IndexError):
            _ = arr[2]

    def test_array_set_item_frozenset(self):
        arr = array(ctype=ctypes.py_object, size=2)
        arr[0] = frozenset({5, 6})
        self.assertEqual(arr[0], frozenset({5, 6}))

    def test_array_with_set(self):
        arr = array(ctype=ctypes.py_object, size=3, iterable=[{1, 2}, {3, 4}])
        self.assertEqual(arr[0], {1, 2})
        self.assertEqual(arr[1], {3, 4})
        with self.assertRaises(IndexError):
            _ = arr[2]

    def test_array_set_item_set(self):
        arr = array(ctype=ctypes.py_object, size=2)
        arr[0] = {5, 6}
        self.assertEqual(arr[0], {5, 6})

    def test_array_extend_with_strings(self):
        arr = array(ctype=ctypes.c_wchar_p, size=5, iterable=["a", "b"])
        arr.extend(["c", "d"])
        self.assertEqual(arr[0], "a")
        self.assertEqual(arr[1], "b")
        self.assertEqual(arr[2], "c")
        self.assertEqual(arr[3], "d")
        with self.assertRaises(IndexError):
            _ = arr[4]

    def test_array_extend_with_complex(self):
        arr = array(ctype=icomplex, size=5, iterable=[icomplex(1, 1), icomplex(2, 2)])
        arr.extend([icomplex(3, 3)])
        self.assertEqual(arr[2], icomplex(3, 3))
        with self.assertRaises(IndexError):
            _ = arr[3]

    def test_array_extend_with_frozenset(self):
        arr = array(
            ctype=ctypes.py_object, size=5, iterable=[frozenset({1}), frozenset({2})]
        )
        arr.extend([frozenset({3}), frozenset({4})])
        self.assertEqual(arr[2], frozenset({3}))
        self.assertEqual(arr[3], frozenset({4}))


if __name__ == "__main__":
    unittest.main()
