import math
import unittest
from .calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up a new calculator instance for each test."""
        self.calc = Calculator()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.divide(10, 2), 5.0)
    
    def test_last_result(self):
        """Test operations using the last_result property."""
        self.calc.clear()
        self.calc.add(10)
        self.assertEqual(self.calc.add(5), 15)
        self.assertEqual(self.calc.subtract(3), 12)
        self.assertEqual(self.calc.multiply(2), 24)
        self.assertEqual(self.calc.divide(6), 4)
    
    def test_power_and_sqrt(self):
        """Test power and square root operations."""
        self.calc.clear()
        self.assertEqual(self.calc.add(9), 9)
        self.assertEqual(self.calc.square_root(), 3)
        self.assertEqual(self.calc.power(2), 9)
    
    def test_memory_operations(self):
        """Test memory operations."""
        self.calc.clear()
        self.calc.add(5)
        self.calc.memory_store()  # Memory = 5
        self.calc.clear()
        self.assertEqual(self.calc.memory_recall(), 5)
        
        self.calc.add(3)  # last_result = 5 + 3 = 8
        self.calc.memory_add()  # Adds last_result (8) to memory (5), making memory = 13
        self.assertEqual(self.calc.memory_recall(), 13)
        
        self.calc.add(2)  # last_result = 13 + 2 = 15
        self.calc.memory_subtract()  # Memory = 13 - 15 = -2
        self.assertEqual(self.calc.memory_recall(), -2)
        self.assertEqual(self.calc.memory_clear(), 0)
    
    def test_scientific_functions(self):
        """Test scientific functions."""
        self.calc.clear()
        self.calc.add(math.pi/2)
        self.assertAlmostEqual(self.calc.sin(), 1.0)
        
        self.calc.clear()
        self.calc.add(0)
        self.assertEqual(self.calc.cos(), 1.0)
        
        self.calc.clear()
        self.calc.add(100)
        self.assertEqual(self.calc.log10(), 2.0)
        
        self.calc.clear()
        self.calc.add(5)
        self.assertEqual(self.calc.factorial(), 120)
    
    def test_error_handling(self):
        """Test error handling for invalid operations."""
        self.calc.clear()
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)
        
        self.calc.add(-4)
        with self.assertRaises(ValueError):
            self.calc.square_root()


if __name__ == "__main__":
    unittest.main() 