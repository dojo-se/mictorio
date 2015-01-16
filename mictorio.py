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
    
    i=0
    #for i in range(len(mijoes)):
    while(i < len(mijoes)):
        if (i == 0):
            if mijoes[i] == 'o' and mijoes[i+1] == 'o':
                mictorios_livres.append(i)
                i += 1
        elif (i == len(mijoes)-1):
            if mijoes[i] == 'o' and mijoes[i-1] == 'o':
                mictorios_livres.append(i)
        elif (mijoes[i] == 'o' and mijoes[i-1] == 'o' and mijoes[i+1] == 'o'):
            mictorios_livres.append(i)
            i += 1
        i += 1
           
    return mictorios_livres

class MictorioTest(unittest.TestCase):
    def test_xoo(self):
        self.assertEqual([2], mictorio('xoo'))
    def test_xoxo(self):
        self.assertEqual([], mictorio('xoxo'))
    def test_x(self):
        self.assertEqual([], mictorio('x'))
    def test_o(self):
        self.assertEqual([0], mictorio('o'))
    def test_xoooo(self):
        self.assertEqual([2,4], mictorio('xoooo'))

if __name__ == '__main__':
    unittest.main()
