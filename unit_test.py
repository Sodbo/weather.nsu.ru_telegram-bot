import unittest
from get_nsu_temp import get_nsu_temp
from get_nsu_temp import message_nsu_temp

class TestStringMethods(unittest.TestCase):

    def test_get_nsu_temp_is_str(self):
        self.assertTrue(isinstance(get_nsu_temp()[0], str))
    
    def test_get_nsu_temp_is_not_empty(self):
        self.assertTrue(len(get_nsu_temp()[0])!=0)

    def test_message_nsu_temp_has_6_words(self):
        self.assertEqual(len(message_nsu_temp('-10C').split(' ')), 6)

if __name__ == '__main__':
    unittest.main()