import unittest
from thealgorithm.abc.list import LinearList, DoublyList, llist, dlist


class TestCreateLinearList(unittest.TestCase):
    def test_llist(self):
        iterable_int = [10, 20, 30]
        new_list_int = llist(iterable_int)
        self.assertEqual(repr(new_list_int), "[ 10 20 30 ]")
        self.assertEqual(len(new_list_int), 3)

        iterable_str = ["apple", "banana", "cherry"]
        new_list_str = llist(iterable_str)
        self.assertEqual(repr(new_list_str), "[ apple banana cherry ]")
        self.assertEqual(len(new_list_str), 3)

        iterable_str = "abc"
        new_list_str = llist(iterable_str)
        self.assertEqual(repr(new_list_str), "[ a b c ]")
        self.assertEqual(len(new_list_str), 3)

        iterable_mixed = [10, "apple", 3.14, True]
        new_list_mixed = llist(iterable_mixed)
        self.assertEqual(repr(new_list_mixed), "[ 10 apple 3.14 True ]")
        self.assertEqual(len(new_list_mixed), 4)

        iterable_dict = [{"key": "value"}, {"name": "Alice"}]
        new_list_dict = llist(iterable_dict)
        self.assertEqual(repr(new_list_dict), "[ {'key': 'value'} {'name': 'Alice'} ]")
        self.assertEqual(len(new_list_dict), 2)

        iterable_set = {1, 2, 3}
        new_list_set = llist(iterable_set)
        self.assertEqual(repr(new_list_set), "[ 1 2 3 ]")
        self.assertEqual(len(new_list_set), 3)

        empty_iterable = []
        empty_list = llist(empty_iterable)
        self.assertEqual(repr(empty_list), "[ ]")
        self.assertEqual(len(empty_list), 0)

        with self.assertRaises(TypeError):
            llist(123)

        with self.assertRaises(TypeError):
            llist(None)


class TestLinearList(unittest.TestCase):
    def setUp(self):
        self.list = LinearList()

    def test_bool(self):
        self.assertFalse(self.list)  # Empty list should evaluate to False
        self.list.append(10)
        self.assertFalse(not self.list)  # Non-empty list should evaluate to False

    def test_push(self):
        llist = LinearList()
        llist.push(10)
        self.assertEqual(repr(llist), "[ 10 ]")
        self.assertEqual(len(llist), 1)

        llist.push(20)
        llist.push(30)
        self.assertEqual(repr(llist), "[ 30 20 10 ]")
        self.assertEqual(len(llist), 3)

    def test_append(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.find(10), 0)
        self.assertEqual(self.list.find(20), 1)
        self.assertEqual(self.list.__repr__(), "[ 10 20 ]")

    def test_insert(self):
        self.list.append(10)
        self.list.append(30)
        self.list.insert(1, 20)  # Insert 20 at index 1
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.find(20), 1)
        self.assertEqual(self.list.__repr__(), "[ 10 20 30 ]")

        with self.assertRaises(IndexError):
            self.list.insert(40, 4)  # Invalid index

    def test_find(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(self.list.find(10), 0)
        self.assertEqual(self.list.find(20), 1)
        self.assertEqual(self.list.find(30), -1)  # Item not in the list

    def test_size(self):
        self.assertEqual(len(self.list), 0)
        self.list.append(10)
        self.assertEqual(len(self.list), 1)
        self.list.append(20)
        self.assertEqual(len(self.list), 2)

    def test_get(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.assertEqual(self.list.get(0), 10)
        self.assertEqual(self.list.get(1), 20)
        self.assertEqual(self.list.get(2), 30)

        with self.assertRaises(IndexError):
            self.list.get(-1)  # Negative index
        with self.assertRaises(IndexError):
            self.list.get(3)  # Index out of range


class TestLinkedListSlice(unittest.TestCase):
    def setUp(self):
        self.ll = LinearList()
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.append(40)

    def test_single_index(self):
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 20)
        self.assertEqual(self.ll[3], 40)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            _ = self.ll[4]
        with self.assertRaises(IndexError):
            _ = self.ll[-1]

    def test_slicing(self):
        self.assertEqual(self.ll[:2], llist([10, 20]))
        self.assertEqual(self.ll[1:3], llist([20, 30]))
        self.assertEqual(self.ll[::2], llist([10, 30]))
        self.assertEqual(self.ll[1:], llist([20, 30, 40]))
        self.assertEqual(self.ll[:], llist([10, 20, 30, 40]))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            _ = self.ll["invalid"]


class TestLinearListExtended(unittest.TestCase):
    def setUp(self):
        self.list = LinearList()

    def test_pop(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)

        self.assertEqual(self.list.pop(), 30)
        self.assertEqual(repr(self.list), "[ 10 20 ]")
        self.assertEqual(len(self.list), 2)

        self.assertEqual(self.list.pop(0), 10)
        self.assertEqual(repr(self.list), "[ 20 ]")
        self.assertEqual(len(self.list), 1)

        self.assertEqual(self.list.pop(0), 20)
        self.assertEqual(repr(self.list), "[ ]")
        self.assertEqual(len(self.list), 0)

        with self.assertRaises(IndexError):
            self.list.pop()

        self.list.append(100)
        self.list.append(200)
        self.list.append(300)

        self.assertEqual(self.list.pop(1), 200)
        self.assertEqual(repr(self.list), "[ 100 300 ]")
        self.assertEqual(len(self.list), 2)

        with self.assertRaises(IndexError):
            self.list.pop(5)

        with self.assertRaises(IndexError):
            self.list.pop(-1)

    def test_remove(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)

        self.list.remove(20)
        self.assertEqual(repr(self.list), "[ 10 30 40 ]")
        self.assertEqual(len(self.list), 3)

        self.list.remove(40)
        self.assertEqual(repr(self.list), "[ 10 30 ]")
        self.assertEqual(len(self.list), 2)

        self.list.remove(10)
        self.assertEqual(repr(self.list), "[ 30 ]")
        self.assertEqual(len(self.list), 1)

        with self.assertRaises(ValueError):
            self.list.remove(50)

        self.list.remove(30)
        self.assertEqual(repr(self.list), "[ ]")
        self.assertEqual(len(self.list), 0)

        with self.assertRaises(ValueError):
            self.list.remove(30)

    def test_replace(self):
        # Test replace on an empty list
        with self.assertRaises(IndexError):
            self.list.replace(0, 10)

        # Test replace on a list with elements
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)

        # Replace first element
        self.list.replace(0, 100)
        self.assertEqual(self.list.__repr__(), "[ 100 20 30 ]")

        # Replace middle element
        self.list.replace(1, 200)
        self.assertEqual(self.list.__repr__(), "[ 100 200 30 ]")

        # Replace last element
        self.list.replace(2, 300)
        self.assertEqual(self.list.__repr__(), "[ 100 200 300 ]")

        # Test invalid index
        with self.assertRaises(IndexError):
            self.list.replace(-1, 400)
        with self.assertRaises(IndexError):
            self.list.replace(3, 500)  # Out of range index

    def test_swap(self):
        # Test swapping two elements
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.swap(0, 2)
        self.assertEqual(repr(self.list), "[ 30 20 10 ]")

        # Test swapping with the same index (no change)
        self.list.swap(1, 1)
        self.assertEqual(repr(self.list), "[ 30 20 10 ]")

        # Test invalid index
        with self.assertRaises(IndexError):
            self.list.swap(0, 3)
        with self.assertRaises(IndexError):
            self.list.swap(-4, -3)

    def test_sort(self):
        self.list.append(40)
        self.list.append(10)
        self.list.append(30)
        self.list.append(20)

        self.list.sort()
        self.assertEqual(repr(self.list), "[ 10 20 30 40 ]")

        self.list.sort(reverse=True)
        self.assertEqual(repr(self.list), "[ 40 30 20 10 ]")

        self.list.clear()
        self.list.append(50)
        self.list.append(10)

        self.list.sort()
        self.assertEqual(repr(self.list), "[ 10 50 ]")

        self.list.sort(reverse=True)
        self.assertEqual(repr(self.list), "[ 50 10 ]")

    def test_delitem(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)

        del self.list[1]
        self.assertEqual(repr(self.list), "[ 10 30 40 ]")
        self.assertEqual(len(self.list), 3)

        del self.list[0]
        self.assertEqual(repr(self.list), "[ 30 40 ]")
        self.assertEqual(len(self.list), 2)

        del self.list[1]
        self.assertEqual(repr(self.list), "[ 30 ]")
        self.assertEqual(len(self.list), 1)

        del self.list[0]
        self.assertEqual(repr(self.list), "[ ]")
        self.assertEqual(len(self.list), 0)

        with self.assertRaises(IndexError):
            del self.list[0]

        with self.assertRaises(IndexError):
            del self.list[-1]

        with self.assertRaises(IndexError):
            del self.list[3]


class TestLinearListIteration(unittest.TestCase):
    def setUp(self):
        self.list = LinearList()

    def test_iteration_empty_list(self):
        result = [item for item in self.list]
        self.assertEqual(result, [])

    def test_iteration_single_element(self):
        self.list.append(10)
        result = [item for item in self.list]
        self.assertEqual(result, [10])

    def test_iteration_multiple_elements(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        result = [item for item in self.list]
        self.assertEqual(result, [10, 20, 30])

    def test_iteration_multiple_times(self):
        self.list.append(10)
        self.list.append(20)
        result1 = [item for item in self.list]
        result2 = [item for item in self.list]
        self.assertEqual(result1, [10, 20])
        self.assertEqual(result2, [10, 20])  # Ensure the iterator resets

    def test_getitem_setitem(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)

        self.assertEqual(self.list[0], 10)
        self.assertEqual(self.list[3], 40)

        with self.assertRaises(IndexError):
            _ = self.list[-1]

        with self.assertRaises(IndexError):
            _ = self.list[4]

        with self.assertRaises(IndexError):
            _ = self.list[-5]

        self.list[0] = 15
        self.assertEqual(self.list[0], 15)

        self.list[3] = 45
        self.assertEqual(self.list[3], 45)

        with self.assertRaises(IndexError):
            self.list[4] = 50

        with self.assertRaises(IndexError):
            self.list[-5] = 50


class TestCreateDoublyList(unittest.TestCase):
    def test_llist(self):
        iterable_int = [10, 20, 30]
        new_list_int = dlist(iterable_int)
        self.assertEqual(repr(new_list_int), "[ 10 20 30 ]")
        self.assertEqual(len(new_list_int), 3)

        iterable_str = ["apple", "banana", "cherry"]
        new_list_str = dlist(iterable_str)
        self.assertEqual(repr(new_list_str), "[ apple banana cherry ]")
        self.assertEqual(len(new_list_str), 3)

        iterable_str = "abc"
        new_list_str = dlist(iterable_str)
        self.assertEqual(repr(new_list_str), "[ a b c ]")
        self.assertEqual(len(new_list_str), 3)

        iterable_mixed = [10, "apple", 3.14, True]
        new_list_mixed = dlist(iterable_mixed)
        self.assertEqual(repr(new_list_mixed), "[ 10 apple 3.14 True ]")
        self.assertEqual(len(new_list_mixed), 4)

        iterable_dict = [{"key": "value"}, {"name": "Alice"}]
        new_list_dict = dlist(iterable_dict)
        self.assertEqual(repr(new_list_dict), "[ {'key': 'value'} {'name': 'Alice'} ]")
        self.assertEqual(len(new_list_dict), 2)

        iterable_set = {1, 2, 3}
        new_list_set = dlist(iterable_set)
        self.assertEqual(repr(new_list_set), "[ 1 2 3 ]")
        self.assertEqual(len(new_list_set), 3)

        empty_iterable = []
        empty_list = dlist(empty_iterable)
        self.assertEqual(repr(empty_list), "[ ]")
        self.assertEqual(len(empty_list), 0)

        with self.assertRaises(TypeError):
            dlist(123)

        with self.assertRaises(TypeError):
            dlist(None)


class TestDoublyList(unittest.TestCase):
    def setUp(self):
        self.dlist = DoublyList()

    def test_push(self):
        self.dlist.push(10)
        self.assertEqual(repr(self.dlist), "[ 10 ]")
        self.dlist.push(20)
        self.dlist.push(30)
        self.assertEqual(repr(self.dlist), "[ 30 20 10 ]")
        self.assertEqual(len(self.dlist), 3)

    def test_append(self):
        self.dlist.append(10)
        self.assertEqual(repr(self.dlist), "[ 10 ]")
        self.dlist.append(20)
        self.dlist.append(30)
        self.assertEqual(repr(self.dlist), "[ 10 20 30 ]")
        self.assertEqual(len(self.dlist), 3)

    def test_clear(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.clear()
        self.assertEqual(len(self.dlist), 0)
        self.assertEqual(repr(self.dlist), "[ ]")

    def test_len(self):
        self.assertEqual(len(self.dlist), 0)
        self.dlist.push(10)
        self.assertEqual(len(self.dlist), 1)
        self.dlist.append(20)
        self.assertEqual(len(self.dlist), 2)

    def test_get(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.assertEqual(self.dlist.get(0), 10)
        self.assertEqual(self.dlist.get(1), 20)
        self.assertEqual(self.dlist.get(2), 30)
        self.assertEqual(self.dlist.get(-1), 30)
        self.assertEqual(self.dlist.get(-2), 20)
        self.assertEqual(self.dlist.get(-3), 10)
        with self.assertRaises(IndexError):
            self.dlist.get(3)
        with self.assertRaises(IndexError):
            self.dlist.get(-4)

    def test_find(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.assertEqual(self.dlist.find(10), 0)
        self.assertEqual(self.dlist.find(20), 1)
        self.assertEqual(self.dlist.find(30), 2)
        self.assertEqual(self.dlist.find(40), -1)

    def test_pop(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.dlist.append(40)

        self.assertEqual(self.dlist.pop(), 40)
        self.assertEqual(repr(self.dlist), "[ 10 20 30 ]")
        self.assertEqual(len(self.dlist), 3)

        self.assertEqual(self.dlist.pop(-1), 30)
        self.assertEqual(repr(self.dlist), "[ 10 20 ]")
        self.assertEqual(len(self.dlist), 2)

        self.assertEqual(self.dlist.pop(0), 10)
        self.assertEqual(repr(self.dlist), "[ 20 ]")
        self.assertEqual(len(self.dlist), 1)

        self.assertEqual(self.dlist.pop(-1), 20)
        self.assertEqual(repr(self.dlist), "[ ]")
        self.assertEqual(len(self.dlist), 0)

        with self.assertRaises(IndexError):
            self.dlist.pop()

        with self.assertRaises(IndexError):
            self.dlist.pop(2)

        with self.assertRaises(IndexError):
            self.dlist.pop(-3)

    def test_remove(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.dlist.append(40)

        self.dlist.remove(20)
        self.assertEqual(repr(self.dlist), "[ 10 30 40 ]")
        self.assertEqual(len(self.dlist), 3)

        self.dlist.remove(40)
        self.assertEqual(repr(self.dlist), "[ 10 30 ]")
        self.assertEqual(len(self.dlist), 2)

        self.dlist.remove(10)
        self.assertEqual(repr(self.dlist), "[ 30 ]")
        self.assertEqual(len(self.dlist), 1)

        with self.assertRaises(ValueError):
            self.dlist.remove(50)

        self.dlist.remove(30)
        self.assertEqual(repr(self.dlist), "[ ]")
        self.assertEqual(len(self.dlist), 0)

        with self.assertRaises(ValueError):
            self.dlist.remove(30)

    def test_insert(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)

        # Insert at the beginning
        self.dlist.insert(0, 5)
        self.assertEqual(repr(self.dlist), "[ 5 10 20 30 ]")
        self.assertEqual(len(self.dlist), 4)

        # Insert in the middle
        self.dlist.insert(2, 15)
        self.assertEqual(repr(self.dlist), "[ 5 10 15 20 30 ]")
        self.assertEqual(len(self.dlist), 5)

        # Insert at the end
        self.dlist.insert(5, 35)
        self.assertEqual(repr(self.dlist), "[ 5 10 15 20 30 35 ]")
        self.assertEqual(len(self.dlist), 6)

        # Insert at negative index
        self.dlist.insert(-1, 25)
        self.assertEqual(repr(self.dlist), "[ 5 10 15 20 30 35 25 ]")
        self.assertEqual(len(self.dlist), 7)

        # Insert at negative index
        self.dlist.insert(-4, -1)
        self.assertEqual(repr(self.dlist), "[ 5 10 15 -1 20 30 35 25 ]")
        self.assertEqual(len(self.dlist), 8)

        # Insert at the beginning (negative index)
        self.dlist.insert(-8, 100)
        self.assertEqual(repr(self.dlist), "[ 100 5 10 15 -1 20 30 35 25 ]")
        self.assertEqual(len(self.dlist), 9)

    def test_replace(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.dlist.append(40)

        self.dlist.replace(1, 25)
        self.assertEqual(repr(self.dlist), "[ 10 25 30 40 ]")

        self.dlist.replace(0, 5)
        self.assertEqual(repr(self.dlist), "[ 5 25 30 40 ]")

        self.dlist.replace(3, 45)
        self.assertEqual(repr(self.dlist), "[ 5 25 30 45 ]")

        self.dlist.replace(-2, 35)
        self.assertEqual(repr(self.dlist), "[ 5 25 35 45 ]")

        with self.assertRaises(IndexError):
            self.dlist.replace(4, 50)

        with self.assertRaises(IndexError):
            self.dlist.replace(-5, 50)

    def test_swap(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.dlist.append(40)

        self.dlist.swap(0, 3)
        self.assertEqual(repr(self.dlist), "[ 40 20 30 10 ]")

        self.dlist.swap(1, 2)
        self.assertEqual(repr(self.dlist), "[ 40 30 20 10 ]")

        self.dlist.swap(-4, -1)
        self.assertEqual(repr(self.dlist), "[ 10 30 20 40 ]")

        with self.assertRaises(IndexError):
            self.dlist.swap(0, 4)

        with self.assertRaises(IndexError):
            self.dlist.swap(-5, 2)

    def test_iteration(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        result = [item for item in self.dlist]
        self.assertEqual(result, [10, 20, 30])

        # Ensure iteration resets
        result_again = [item for item in self.dlist]
        self.assertEqual(result_again, [10, 20, 30])

    def test_getitem_setitem(self):
        self.dlist = [10, 20, 30, 40]

        self.assertEqual(self.dlist[0], 10)
        self.assertEqual(self.dlist[3], 40)
        self.assertEqual(self.dlist[-1], 40)
        self.assertEqual(self.dlist[-4], 10)

        with self.assertRaises(IndexError):
            _ = self.dlist[4]

        with self.assertRaises(IndexError):
            _ = self.dlist[-5]

        self.dlist[0] = 15
        self.assertEqual(self.dlist[0], 15)

        self.dlist[3] = 45
        self.assertEqual(self.dlist[3], 45)

        self.dlist[-2] = 35
        self.assertEqual(self.dlist[2], 35)

        with self.assertRaises(IndexError):
            self.dlist[4] = 50

        with self.assertRaises(IndexError):
            self.dlist[-5] = 50

    def test_sort(self):
        self.dlist.append(40)
        self.dlist.append(10)
        self.dlist.append(30)
        self.dlist.append(20)

        self.dlist.sort()
        self.assertEqual(repr(self.dlist), "[ 10 20 30 40 ]")

        self.dlist.sort(reverse=True)
        self.assertEqual(repr(self.dlist), "[ 40 30 20 10 ]")

        self.dlist.clear()
        self.dlist.append(50)
        self.dlist.append(10)

        self.dlist.sort()
        self.assertEqual(repr(self.dlist), "[ 10 50 ]")

        self.dlist.sort(reverse=True)
        self.assertEqual(repr(self.dlist), "[ 50 10 ]")

    def test_delitem(self):
        self.dlist.append(10)
        self.dlist.append(20)
        self.dlist.append(30)
        self.dlist.append(40)

        del self.dlist[1]
        self.assertEqual(repr(self.dlist), "[ 10 30 40 ]")
        self.assertEqual(len(self.dlist), 3)

        del self.dlist[0]
        self.assertEqual(repr(self.dlist), "[ 30 40 ]")
        self.assertEqual(len(self.dlist), 2)

        del self.dlist[-1]
        self.assertEqual(repr(self.dlist), "[ 30 ]")
        self.assertEqual(len(self.dlist), 1)

        del self.dlist[-1]
        self.assertEqual(repr(self.dlist), "[ ]")
        self.assertEqual(len(self.dlist), 0)

        with self.assertRaises(IndexError):
            del self.dlist[0]

        with self.assertRaises(IndexError):
            del self.dlist[-1]


class TestDoublyListSlice(unittest.TestCase):
    def setUp(self):
        self.dl = DoublyList()
        self.dl.append(10)
        self.dl.append(20)
        self.dl.append(30)
        self.dl.append(40)

    def test_single_index(self):
        self.assertEqual(self.dl[0], 10)
        self.assertEqual(self.dl[1], 20)
        self.assertEqual(self.dl[3], 40)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            _ = self.dl[4]

    def test_slicing(self):
        self.assertEqual(self.dl[:2], [10, 20])
        self.assertEqual(self.dl[1:3], [20, 30])
        self.assertEqual(self.dl[::2], [10, 30])
        self.assertEqual(self.dl[1:], [20, 30, 40])
        self.assertEqual(self.dl[:], [10, 20, 30, 40])

    def test_negative_index(self):
        self.assertEqual(self.dl[-1], 40)
        self.assertEqual(self.dl[-2], 30)
        self.assertEqual(self.dl[-4], 10)
        with self.assertRaises(IndexError):
            _ = self.dl[-5]

    def test_negative_slicing(self):
        self.assertEqual(self.dl[-3:], [20, 30, 40])
        self.assertEqual(self.dl[-4:-1], [10, 20, 30])
        self.assertEqual(self.dl[::-1], [40, 30, 20, 10])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            _ = self.dl["invalid"]
