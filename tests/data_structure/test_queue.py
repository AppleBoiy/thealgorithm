import unittest
from thealgorithm.abc import queue


class TestQueue(unittest.TestCase):
    def test_initialization(self):
        q = queue()
        self.assertEqual(len(q), 0)
        self.assertTrue(q._head is None)
        self.assertTrue(q._tail is None)

    def test_initialization_with_values(self):
        q = queue([1, 2, 3])
        self.assertEqual(len(q), 3)
        self.assertEqual(list(q), [1, 2, 3])

    def test_initialization_invalid_values(self):
        with self.assertRaises(TypeError):
            queue(123)

    def test_enqueue(self):
        q = queue()
        q.enqueue(10)
        self.assertEqual(len(q), 1)
        self.assertEqual(q._head.value, 10)
        q.enqueue(20)
        self.assertEqual(len(q), 2)
        self.assertEqual(q._head.value, 10)
        self.assertEqual(q._tail.value, 20)

    def test_dequeue(self):
        q = queue([1, 2, 3])
        value = q.dequeue()
        self.assertEqual(value, 1)
        self.assertEqual(len(q), 2)
        self.assertEqual(list(q), [2, 3])

    def test_dequeue_empty(self):
        q = queue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_clear(self):
        q = queue([1, 2, 3])
        q.clear()
        self.assertEqual(len(q), 0)
        self.assertTrue(q._head is None)

    def test_extend(self):
        q = queue()
        q.extend([4, 5, 6])
        self.assertEqual(len(q), 3)
        self.assertEqual(list(q), [4, 5, 6])

    def test_extend_with_overflow(self):
        q = queue(size=5)
        q.extend([1, 2, 3])
        with self.assertRaises(OverflowError):
            q.extend([4, 5, 6])

    def test_extend_invalid_values(self):
        q = queue()
        with self.assertRaises(TypeError):
            q.extend(123)
        with self.assertRaises(TypeError):
            q.extend(None)
        with self.assertRaises(TypeError):
            q.extend(0b10)

    def test_iteration(self):
        q = queue([1, 2, 3])
        values = list(iter(q))
        self.assertEqual(values, [1, 2, 3])

    def test_repr(self):
        q = queue([1, 2, 3])
        self.assertEqual(repr(q), "Queue(1, 2, 3)")

    def test_enqueue_with_overflow(self):
        q = queue(size=2)
        q.enqueue(1)
        q.enqueue(2)
        with self.assertRaises(OverflowError):
            q.enqueue(3)


if __name__ == "__main__":
    unittest.main()
