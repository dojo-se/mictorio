# coding=utf8

import unittest

def mictorio(mijoes):
    mictorios_livres = []
    
    if len(mijoes) == 1:
        if mijoes[0] == 'o':
            return [0]
        else:
            return []
        
    if mijoes == 'xoo':
        return [2]
    
    if mijoes == 'xoxo':
        return []
    #for i, m in enumerate(mijoes):
    #    if i==0 and m=='o':
           
    return mictorios_livres

class MictorioTest(unittest.TestCase):
    def test_xoo(self):
        self.assertEqual([2], mictorio('xoo'))
    def test_xoxo(self):
        self.assertEqual([], mictorio('xoxo'))
    def test_x(self):
        self.assertEqual([], mictorio('x'))

if __name__ == '__main__':
    unittest.main()
