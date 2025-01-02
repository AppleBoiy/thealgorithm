import unittest
from thealgorithm.abc.sequence import MutSequence


class TestMutSequence(unittest.TestCase):
    def test_sequence_len(self):
        seq = MutSequence()
        self.assertEqual(len(seq), 0)

    def test_sequence_bool(self):
        seq = MutSequence()
        self.assertFalse(bool(seq))
        seq._size = 1
        self.assertTrue(bool(seq))

    def test_sequence_find(self):
        seq = MutSequence()

        with self.assertRaises(NotImplementedError):
            seq.find(2)


if __name__ == "__main__":
    unittest.main()
