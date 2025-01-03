import unittest

from thealgorithm.abc.node import PriorityNode


class TestPriorityNode(unittest.TestCase):
    def setUp(self):
        self.node1 = PriorityNode(value="Task1", _priority=5)
        self.node2 = PriorityNode(value="Task2", _priority=10)
        self.node3 = PriorityNode(value="Task1", _priority=5)
        self.node4 = PriorityNode(value="Task3", _priority=1)

    def test_initialization(self):
        node = PriorityNode(value="Test", _priority=20)
        self.assertEqual(node.value, "Test")
        self.assertEqual(node.priority, 20)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

    def test_default_priority(self):
        node = PriorityNode(value="DefaultPriority")
        self.assertEqual(node.priority, float("-inf"))

    def test_repr(self):
        self.assertEqual(repr(self.node1), "PriorityNode(5: 'Task1')")
        self.assertEqual(repr(self.node2), "PriorityNode(10: 'Task2')")

    def test_comparison_lt(self):
        self.assertTrue(self.node1 < self.node2)
        self.assertFalse(self.node2 < self.node1)

    def test_comparison_gt(self):
        self.assertTrue(self.node2 > self.node1)
        self.assertFalse(self.node1 > self.node2)

    def test_comparison_eq(self):
        self.assertTrue(self.node1 == self.node3)
        self.assertFalse(self.node1 == self.node2)

    def test_comparison_ne(self):
        self.assertTrue(self.node1 != self.node2)
        self.assertFalse(self.node1 != self.node3)

    def test_comparison_le(self):
        self.assertTrue(self.node1 <= self.node3)  # Equal priority and value
        self.assertTrue(self.node4 <= self.node1)  # Lower priority
        self.assertFalse(self.node2 <= self.node1)  # Higher priority

    def test_comparison_ge(self):
        self.assertTrue(self.node1 >= self.node3)  # Equal priority and value
        self.assertTrue(self.node2 >= self.node1)  # Higher priority
        self.assertFalse(self.node4 >= self.node1)  # Lower priority

    def test_comparison_same_priority_different_value(self):
        node_a = PriorityNode(value="A", _priority=5)
        node_b = PriorityNode(value="B", _priority=5)
        self.assertTrue(node_a < node_b)  # Lexicographical order of values
        self.assertFalse(node_b < node_a)


if __name__ == "__main__":
    unittest.main()
