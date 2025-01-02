import unittest
from thealgorithm.abc.base import MutSequence


class TestMutSequence(unittest.TestCase):
    def test_sequence_len(self):
        seq = MutSequence()
        self.assertEqual(len(seq), 0)

    def test_sequence_bool(self):
        seq = MutSequence()
        self.assertFalse(bool(seq))
        seq._size = 1
        self.assertTrue(bool(seq))


if __name__ == "__main__":
    unittest.main()
