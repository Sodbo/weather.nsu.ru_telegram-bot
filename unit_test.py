import unittest
from get_nsu_temp import get_nsu_temp

class TestStringMethods(unittest.TestCase):

    def test_get_nsu_temp_is_str(self):
        self.assertTrue(isinstance(get_nsu_temp(), str))

    def test_get_nsu_temp_has_5_words(self):
        self.assertEqual(len(get_nsu_temp().split(' ')), 6)

if __name__ == '__main__':
    unittest.main()