import unittest
from thealgorithm.abc import stack


class TestStackPush(unittest.TestCase):

    def setUp(self):
        self.stack = stack(size=3)

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
        self.stack = stack(size=3)
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
        with self.assertRaises(OverflowError):
            self.stack.push(40)
        popped_value = self.stack.pop()  # Pops 30
        self.assertEqual(popped_value, 30)
        self.assertEqual(len(self.stack), 2)


class TestStackExtended(unittest.TestCase):

    def setUp(self):
        self.stack = stack()
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


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = stack(size=3)

    def test_init_empty(self):
        self.stack = stack()
        self.assertEqual(len(self.stack), 0)
        self.assertIsNone(self.stack.peek())

    def test_init_with_values(self):
        self.stack = stack([1, 2, 3])
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_init_by_string(self):
        self.stack = stack("abc")
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(self.stack.pop(), "c")
        self.assertEqual(self.stack.pop(), "b")
        self.assertEqual(self.stack.pop(), "a")

    def test_push(self):
        self.stack = stack()
        self.stack.push(10)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.peek(), 10)

    def test_pop(self):
        self.stack = stack([1, 2, 3])
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(len(self.stack), 0)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack = stack([1, 2, 3])
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 2)

    def test_clear(self):
        s = stack([1, 2, 3])
        s.clear()
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.peek())

    def test_max_size(self):
        s = stack(size=3)
        s.push(1)
        s.push(2)
        s.push(3)
        with self.assertRaises(OverflowError):
            s.push(4)

    def test_extend(self):
        s = stack(size=5)
        s.extend([1, 2])
        self.assertEqual(len(s), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_extend_overflow(self):
        s = stack(size=3)
        s.extend([1, 2])
        with self.assertRaises(OverflowError):
            s.extend([3, 4])

    def test_extend_with_non_iterable(self):
        s = stack()
        with self.assertRaises(TypeError):
            s.extend(10)  # Passing a non-iterable

    def test_repr(self):
        s = stack([1, 2, 3], size=5)
        self.assertEqual(repr(s), "Stack(3 2 1)")
        s.pop()
        self.assertEqual(repr(s), "Stack(2 1)")
        s.clear()
        self.assertEqual(repr(s), "Stack()")


if __name__ == "__main__":
    unittest.main()
