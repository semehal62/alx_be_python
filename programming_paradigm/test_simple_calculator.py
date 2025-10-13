import unittest
from simple_calculator import SimpleCalculator

class test_Simplecalculator(unitest.TestCase)
    def setup():
        calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(10,5),15)
        self.assertEqual(self.calc.add(-1,5),4)
        self.assertEqual(self.calc.add(0,0),0)
    def test_subtract(self):
        self.assertEqual(self.calc.add(10,5),5)
        self.assertEqual(self.calc.add(1,1),0)
        self.assertEqual(self.calc.add(1,-1),2)

    def test_multiply(self):
        self.assertEqual(self.calc.add(10,5),150)
        self.assertEqual(self.calc.add(10,0),0)
        self.assertEqual(self.calc.add(0,0),0)

    def test_divide(self):
        self.assertEqual(self.calc.add(10,5),2)
        self.assertEqual(self.calc.add(10,10),1)
        self.assertEqual(self.calc.add(10,5),"None")

if _ _name_ _ == '_ _main_ _':
    unittest.main()
