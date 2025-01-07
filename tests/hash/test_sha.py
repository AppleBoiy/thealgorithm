import unittest
from hashlib import sha1 as hashlib_sha1, sha256 as hashlib_sha256
from thealgorithm.hash import sha1 as my_sha1, sha256 as my_sha256
import requests


class TestSHA(unittest.TestCase):

    SHAS = {
        1: {"test": my_sha1, "valid": hashlib_sha1},
        256: {"test": my_sha256, "valid": hashlib_sha256},
    }

    def test_custom_vs_hashlib(self):
        messages = [
            b"",
            b"Hello",
            b"abc",
            b"The quick brown fox jumps over the lazy dog",
            b"The quick brown fox jumps over the lazy dog.",
        ]

        for b in self.SHAS:
            for message in messages:
                with self.subTest(message=message):
                    custom_result = self.SHAS[b]["test"](message)
                    hashlib_result = self.SHAS[b]["valid"](message).digest()
                    self.assertEqual(
                        custom_result,
                        hashlib_result,
                        f"SHA{b}: {custom_result} != {hashlib_result}",
                    )

    def test_large_text(self):
        url = "https://gist.githubusercontent.com/AppleBoiy/c714c6411b0874095ede6b58364e2134/raw/b660e193c1b77b97c85c0f0e528727ee3f40c1e1/large_file_text.txt"
        response = requests.get(url)
        message = response.content
        for b in self.SHAS:
            with self.subTest(message=message):
                custom_result = self.SHAS[b]["test"](message)
                hashlib_result = self.SHAS[b]["valid"](message).digest()
                self.assertEqual(
                    custom_result,
                    hashlib_result,
                    f"SHA{b}: {custom_result} != {hashlib_result}",
                )


if __name__ == "__main__":
    unittest.main()
