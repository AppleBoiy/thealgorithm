import unittest
from thealgorithm.abc.stack import Stack


class TestStackPush(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(size=3)

    def test_push_single_element(self):
        self.stack.push(10)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack._head.value, 10)

    def test_push_multiple_elements(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(self.stack._head.value, 30)

    def test_push_overflow(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        with self.assertRaises(OverflowError) as context:
            self.stack.push(40)
        self.assertEqual(
            str(context.exception), "the stack has reached its maximum capacity."
        )

    def test_empty_stack(self):
        self.assertEqual(len(self.stack), 0)
        self.assertIsNone(self.stack._head)


class TestStackPop(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(size=3)
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)

    def test_pop_single_element(self):
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 30)  # Last pushed element should be popped
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack._head.value, 20)

    def test_pop_multiple_elements(self):
        popped_value1 = self.stack.pop()
        self.assertEqual(popped_value1, 30)
        self.assertEqual(len(self.stack), 2)

        popped_value2 = self.stack.pop()
        self.assertEqual(popped_value2, 20)
        self.assertEqual(len(self.stack), 1)

    def test_pop_empty_stack(self):
        # Pop all elements to empty the stack
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()

        with self.assertRaises(IndexError) as context:
            self.stack.pop()  # Pop from an empty stack
        self.assertEqual(str(context.exception), "pop from empty stack")

    def test_pop_after_overflow(self):
        with self.assertRaises(OverflowError) as context:
            self.stack.push(40)
        popped_value = self.stack.pop()  # Pops 30
        self.assertEqual(popped_value, 30)
        self.assertEqual(len(self.stack), 2)


class TestStackExtended(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)

    def test_peek_non_empty_stack(self):
        self.assertEqual(
            self.stack.peek(), 30
        )  # Should return the top element without removing it

    def test_peek_empty_stack(self):
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertIsNone(self.stack.peek())  # Should return None for an empty stack

    def test_clear_non_empty_stack(self):
        self.stack.clear()
        self.assertFalse(self.stack)  # Should be empty after clearing
        self.assertEqual(len(self.stack), 0)


if __name__ == "__main__":
    unittest.main()
