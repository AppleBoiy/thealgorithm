import unittest
from hashlib import sha1 as hashlib_sha1
from thealgorithm.hash import sha1 as my_sha1
import requests


class TestSHA1(unittest.TestCase):

    def test_custom_vs_hashlib(self):
        messages = [
            b"",
            b"Hello",
            b"abc",
            b"The quick brown fox jumps over the lazy dog",
            b"The quick brown fox jumps over the lazy dog.",
        ]
        for message in messages:
            with self.subTest(message=message):
                custom_result = my_sha1(message)
                hashlib_result = hashlib_sha1(message).digest()
                self.assertEqual(custom_result, hashlib_result)

    def test_large_text(self):
        url = "https://gist.githubusercontent.com/AppleBoiy/c714c6411b0874095ede6b58364e2134/raw/b660e193c1b77b97c85c0f0e528727ee3f40c1e1/large_file_text.txt"
        response = requests.get(url)
        message = response.content
        custom_result = my_sha1(message)
        hashlib_result = hashlib_sha1(message).digest()
        self.assertEqual(custom_result, hashlib_result)


if __name__ == "__main__":
    unittest.main()
