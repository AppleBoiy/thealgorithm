import unittest

from thealgorithm.abc.node import PriorityNode
from thealgorithm.sorting import heap


class TestHeapFunctions(unittest.TestCase):

    def test_heap_sort_ascending(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed for ascending order.")

    def test_heap_sort_descending(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = sorted(arr, reverse=True)
        heap(arr, reverse=True)
        self.assertEqual(arr, expected, "Heap sort failed for descending order.")

    def test_heap_with_negative_numbers(self):
        arr = [3, -1, 4, -1, -5, 9, 2, 6, -5, 3]
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with negative numbers.")

    def test_heap_with_duplicates(self):
        arr = [5, 1, 5, 1, 5, 1]
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with duplicate numbers.")

    def test_heap_with_floats(self):
        arr = [3.1, 2.4, 5.5, 1.1, 4.8]
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with floating-point numbers.")

    def test_heap_with_strings(self):
        arr = ["banana", "apple", "cherry", "date"]
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(
            arr, expected, "Heap sort failed with strings in ascending order."
        )

        expected_reverse = sorted(arr, reverse=True)
        heap(arr, reverse=True)
        self.assertEqual(
            arr, expected_reverse, "Heap sort failed with strings in descending order."
        )

    def test_heap_with_empty_list(self):
        arr = []
        expected = []
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with an empty list.")

    def test_heap_with_single_element(self):
        arr = [42]
        expected = [42]
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with a single element.")

    def test_heap_custom_objects(self):
        class CustomObject:
            def __init__(self, value):
                self.value = value

            def __lt__(self, other):
                return self.value < other.value

            def __gt__(self, other):
                return self.value > other.value

            def __eq__(self, other):
                return self.value == other.value

            def __repr__(self):
                return f"CustomObject({self.value})"

        arr = [CustomObject(5), CustomObject(1), CustomObject(3)]
        expected = sorted(arr, key=lambda x: x.value)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with custom objects.")

    def test_heap_with_large_data(self):
        arr = list(range(10000, 0, -1))
        expected = sorted(arr)
        heap(arr)
        self.assertEqual(arr, expected, "Heap sort failed with a large dataset.")


class TestHeapWithPriorityNodes(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            PriorityNode(value="Task1", _priority=5),
            PriorityNode(value="Task2", _priority=10),
            PriorityNode(value="Task3", _priority=1),
            PriorityNode(value="Task4", _priority=7),
        ]

    def test_heap_sort_ascending(self):
        heap(self.nodes)  # Default is ascending
        expected = sorted(self.nodes, key=lambda x: x.priority)
        self.assertEqual(
            self.nodes,
            expected,
            "Heap sort failed for PriorityNode in ascending order.",
        )

    def test_heap_sort_descending(self):
        heap(self.nodes, reverse=True)
        expected = sorted(self.nodes, key=lambda x: x.priority, reverse=True)
        self.assertEqual(
            self.nodes,
            expected,
            "Heap sort failed for PriorityNode in descending order.",
        )

    def test_heap_with_equal_priorities(self):
        nodes = [
            PriorityNode(value="Task1", _priority=5),
            PriorityNode(value="Task2", _priority=5),
            PriorityNode(value="Task3", _priority=5),
        ]
        heap(nodes)
        expected = sorted(nodes, key=lambda x: (x.priority, x.value))
        self.assertEqual(nodes, expected, "Heap sort failed with equal priorities.")

    def test_heap_with_empty_list(self):
        nodes = []
        heap(nodes)
        self.assertEqual(nodes, [], "Heap sort failed with an empty list.")

    def test_heap_with_single_element(self):
        nodes = [PriorityNode(value="SingleTask", _priority=1)]
        heap(nodes)
        self.assertEqual(
            nodes,
            [PriorityNode(value="SingleTask", _priority=1)],
            "Heap sort failed with a single element.",
        )

    def test_heap_does_not_mutate_input_structure(self):
        original = self.nodes[:]
        heap(self.nodes)
        self.assertNotEqual(self.nodes, original, "Heap should reorder the input list.")


if __name__ == "__main__":
    unittest.main()
