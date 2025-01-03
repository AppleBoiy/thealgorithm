import unittest
from thealgorithm.abc import priority_queue


class TestPriorityQueue(unittest.TestCase):
    def test_initialization(self):
        pq = priority_queue()
        self.assertEqual(len(pq), 0)
        self.assertTrue(pq._head is None)

    def test_initialization_with_values(self):
        pq = priority_queue([(1, 10), (2, 20), (0, 5)])
        self.assertEqual(len(pq), 3)
        self.assertEqual(pq.dequeue(), 20)  # Highest priority dequeued first

    def test_enqueue(self):
        pq = priority_queue()
        pq.enqueue(10, priority=1)
        self.assertEqual(len(pq), 1)
        self.assertEqual(pq.peek(), 10)
        pq.enqueue(20, priority=2)
        self.assertEqual(len(pq), 2)
        self.assertEqual(pq.peek(), 20)  # Higher priority element at the front

    def test_enqueue_without_priority(self):
        pq = priority_queue()
        pq.enqueue(5)
        pq.enqueue(10, priority=1)
        self.assertEqual(len(pq), 2)
        self.assertEqual(pq.peek(), 10)

    def test_dequeue(self):
        pq = priority_queue([(1, 10), (2, 20), (0, 5)])
        self.assertEqual(pq.dequeue(), 20)  # Highest priority
        self.assertEqual(pq.dequeue(), 10)  # Next highest
        self.assertEqual(pq.dequeue(), 5)  # Lowest priority
        self.assertEqual(len(pq), 0)

    def test_dequeue_empty(self):
        pq = priority_queue()
        with self.assertRaises(IndexError):
            pq.dequeue()

    def test_peek(self):
        pq = priority_queue([(1, 10), (2, 20)])
        self.assertEqual(pq.peek(), 20)
        self.assertEqual(len(pq), 2)  # Peek does not remove

    def test_clear(self):
        pq = priority_queue([(1, 10), (2, 20)])
        pq.clear()
        self.assertEqual(len(pq), 0)
        self.assertTrue(pq._head is None)

    def test_extend(self):
        pq = priority_queue()
        pq.extend([(1, 10), (3, 30)])
        self.assertEqual(len(pq), 2)
        self.assertEqual(pq.dequeue(), 30)

    def test_extend_with_overflow(self):
        pq = priority_queue(size=3)
        pq.extend([(1, 10), (2, 20)])
        with self.assertRaises(OverflowError):
            pq.extend([(3, 30), (4, 40)])

    def test_iteration(self):
        pq = priority_queue([(1, 10), (3, 30)])
        values = list(pq)
        self.assertEqual(values, [30, 10])  # Ordered by priority

    def test_repr(self):
        pq = priority_queue([(1, 10), (2, 20)])
        self.assertEqual(repr(pq), "PriorityQueue(2: 20, 1: 10)")

    def test_enqueue_with_overflow(self):
        pq = priority_queue(size=2)
        pq.enqueue(10, priority=1)
        pq.enqueue(20, priority=2)
        with self.assertRaises(OverflowError):
            pq.enqueue(5, priority=3)


if __name__ == "__main__":
    unittest.main()
