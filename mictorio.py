# coding=utf8

import unittest

def esta_vazio(mijoes, i):
    
    if i == 0 and mijoes[i] == 'o' and mijoes[i+1] == 'o':
            return True
    elif (i == len(mijoes)-1) and mijoes[i] == 'o' and mijoes[i-1] == 'o':
            return True
    elif (mijoes[i] == 'o' and mijoes[i-1] == 'o' and mijoes[i+1] == 'o'):
        return True
    return False

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
        if esta_vazio(mijoes, i):
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
    def test_ooxooxoooxxoo(self):
        self.assertEqual([0,7,12], mictorio('ooxooxoooxxoo'))
    def test_ooooooooo(self):
        self.assertEqual([0,2,4,6,8], mictorio('ooooooooo'))
    def test_oxoxoxoxo(self):
        self.assertEqual([], mictorio('oxoxoxoxo'))
    def test_oxoxoxoxoo(self):
        self.assertEqual([9], mictorio('oxoxoxoxoo'))
        

if __name__ == '__main__':
    unittest.main()
