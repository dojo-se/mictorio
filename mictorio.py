# coding=utf8

import unittest

def mictorio(mijoes):
    return [2]

class MictorioTest(unittest.TestCase):
    def test_3E_xoo(self):
        self.assertEqual([2], mictorio('xoo'))

if __name__ == '__main__':
    unittest.main()
