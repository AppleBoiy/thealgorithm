import unittest
import requests
from thealgorithm.hash import md2


class TestMD2(unittest.TestCase):

    def test_md2_empty_string(self):
        msg = b""
        expect = "8350e5a3e24c153df2275c9f80692773"
        result = md2(msg).hex()
        self.assertEqual(result, expect)

    def test_md2_non_empty_string(self):
        msg = b"hello"
        expect = "a9046c73e00331af68917d3804f70655"
        result = md2(msg).hex()
        self.assertEqual(result, expect)

    def test_md2_with_padded_string(self):
        msg = b"              hello"
        expect = "a890166a9db0402fff84c4713ccbd209"
        result = md2(msg).hex()
        self.assertEqual(result, expect)

    def test_md2_with_large_input(self):
        msg = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        expect = "51175b5fa4e8edf28c20c67e4e1b0005"
        result = md2(msg).hex()
        self.assertEqual(result, expect)

    def test_md2_with_xxxlarge_file(self):
        url = "https://gist.githubusercontent.com/AppleBoiy/c714c6411b0874095ede6b58364e2134/raw/b660e193c1b77b97c85c0f0e528727ee3f40c1e1/large_file_text.txt"
        reponse = requests.get(url)
        msg = reponse.content
        expect = "1b84af93e7089458d476f0717985ff4d"
        result = md2(msg).hex()
        self.assertEqual(result, expect, expect)


if __name__ == "__main__":
    unittest.main()
