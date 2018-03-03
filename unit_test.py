import unittest
from get_nsu_temp import get_nsu_temp

class TestStringMethods(unittest.TestCase):

    def test_get_nsu_temp(self):
        self.assertTrue(isinstance(get_nsu_temp(), str))

if __name__ == '__main__':
    unittest.main()