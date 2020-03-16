"""Unit tests."""

import unittest

import smart


class SmartTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.smart1 = "Fake News @CNN is reporting that I am “still using personal cell phone for calls despite repeated security warnings.”"
        cls.smart2 = "It’s a small, infuriating difference."

    def test_substitute(self):
        result = smart.substitute(self.smart1)
        self.assertEqual(
            result,
            'Fake News @CNN is reporting that I am "still using personal cell phone for calls despite repeated security warnings."',
        )
        result = smart.substitute(self.smart2)
        self.assertEqual(result, "It's a small, infuriating difference.")

    def test_remove(self):
        result = smart.remove(self.smart1)
        self.assertEqual(
            result,
            "Fake News @CNN is reporting that I am still using personal cell phone for calls despite repeated security warnings.",
        )
        result = smart.remove(self.smart2)
        self.assertEqual(result, "Its a small, infuriating difference.")


if __name__ == "__main__":
    unittest.main()
