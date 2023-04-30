import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):

    def test_frenchtoenglish_is_not_null(self):
        self.assertIsNotNone(french_to_english("Bonjour"))

    def test_englishtofrench_is_not_null(self):
        self.assertIsNotNone(english_to_french("hello"))

    def test_frenchtoenglish_is_hello(self):
        self.assertEquals(french_to_english("Bonjour"), "Hello")

    def test_englishtofrench_is_bonjour(self):
        self.assertEquals(english_to_french("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
    