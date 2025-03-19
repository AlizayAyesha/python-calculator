import math
from typing import Optional

class Calculator:
    """
    A comprehensive calculator class with basic and advanced mathematical operations.
    """
    
    def __init__(self) -> None:
        """Initialize the calculator with an empty memory."""
        self.memory: float = 0
        self.last_result: float = 0
    
    def add(self, a: float, b: Optional[float] = None) -> float:
        """Add two numbers or add a number to the last result."""
        if b is None:
            result = self.last_result + a
        else:
            result = a + b
        self.last_result = result
        return result
    
    def subtract(self, a: float, b: Optional[float] = None) -> float:
        """Subtract b from a or subtract a from the last result."""
        if b is None:
            result = self.last_result - a
        else:
            result = a - b
        self.last_result = result
        return result
    
    def multiply(self, a: float, b: Optional[float] = None) -> float:
        """Multiply two numbers or multiply the last result by a."""
        if b is None:
            result = self.last_result * a
        else:
            result = a * b
        self.last_result = result
        return result
    
    def divide(self, a: float, b: Optional[float] = None) -> float:
        """Divide a by b or divide the last result by a."""
        if b is None:
            if a == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = self.last_result / a
        else:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        self.last_result = result
        return result
    
    def power(self, a: float, b: Optional[float] = None) -> float:
        """Calculate a raised to power b, or last result raised to power a."""
        if b is None:
            result = self.last_result ** a
        else:
            result = a ** b
        self.last_result = result
        return result
    
    def square_root(self, a: Optional[float] = None) -> float:
        """Calculate the square root of a number or the last result."""
        if a is None:
            if self.last_result < 0:
                raise ValueError("Cannot calculate square root of negative number")
            result = math.sqrt(self.last_result)
        else:
            if a < 0:
                raise ValueError("Cannot calculate square root of negative number")
            result = math.sqrt(a)
        self.last_result = result
        return result
    
    def modulo(self, a: float, b: Optional[float] = None) -> float:
        """Calculate remainder when a is divided by b, or last result divided by a."""
        if b is None:
            if a == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = self.last_result % a
        else:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a % b
        self.last_result = result
        return result
    
    # Memory operations
    def memory_store(self) -> float:
        """Store the last result in memory."""
        self.memory = self.last_result
        return self.memory
    
    def memory_recall(self) -> float:
        """Recall the value stored in memory."""
        self.last_result = self.memory
        return self.memory
    
    def memory_clear(self) -> float:
        """Clear the memory."""
        self.memory = 0
        return self.memory
    
    def memory_add(self) -> float:
        """Add last result to memory."""
        self.memory += self.last_result
        return self.memory
    
    def memory_subtract(self) -> float:
        """Subtract last result from memory."""
        self.memory -= self.last_result
        return self.memory
    
    # Scientific functions
    def sin(self, angle: Optional[float] = None) -> float:
        """Calculate sine of an angle in radians."""
        if angle is None:
            result = math.sin(self.last_result)
        else:
            result = math.sin(angle)
        self.last_result = result
        return result
    
    def cos(self, angle: Optional[float] = None) -> float:
        """Calculate cosine of an angle in radians."""
        if angle is None:
            result = math.cos(self.last_result)
        else:
            result = math.cos(angle)
        self.last_result = result
        return result
    
    def tan(self, angle: Optional[float] = None) -> float:
        """Calculate tangent of an angle in radians."""
        if angle is None:
            result = math.tan(self.last_result)
        else:
            result = math.tan(angle)
        self.last_result = result
        return result
    
    def log10(self, a: Optional[float] = None) -> float:
        """Calculate base-10 logarithm of a number."""
        if a is None:
            if self.last_result <= 0:
                raise ValueError("Cannot calculate logarithm of non-positive number")
            result = math.log10(self.last_result)
        else:
            if a <= 0:
                raise ValueError("Cannot calculate logarithm of non-positive number")
            result = math.log10(a)
        self.last_result = result
        return result
    
    def ln(self, a: Optional[float] = None) -> float:
        """Calculate natural logarithm of a number."""
        if a is None:
            if self.last_result <= 0:
                raise ValueError("Cannot calculate logarithm of non-positive number")
            result = math.log(self.last_result)
        else:
            if a <= 0:
                raise ValueError("Cannot calculate logarithm of non-positive number")
            result = math.log(a)
        self.last_result = result
        return result
    
    def factorial(self, n: Optional[int] = None) -> int:
        """Calculate factorial of n."""
        if n is None:
            n = int(self.last_result)
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial requires a non-negative integer")
        result = math.factorial(n)
        self.last_result = float(result)
        return result
    
    def clear(self) -> float:
        """Clear the last result."""
        self.last_result = 0
        return self.last_result


# Example usage
"""
Example usage of the Calculator class:

# Create a calculator instance
calc = Calculator()

# Basic arithmetic operations
calc.add(5, 3)         # Returns: 8
calc.subtract(10, 4)    # Returns: 6
calc.multiply(3, 4)     # Returns: 12
calc.divide(10, 2)      # Returns: 5.0

# Using the last result
calc.add(5, 3)          # Sets last_result to 8
calc.add(2)             # 8 + 2 = 10
calc.multiply(3)        # 10 * 3 = 30

# Scientific functions
calc.clear()            # Reset to 0
calc.add(math.pi/2)     # Sets to π/2
calc.sin()              # sin(π/2) = 1.0
calc.clear()
calc.add(100)
calc.log10()            # log10(100) = 2.0

# Memory operations
calc.clear()
calc.add(5)
calc.memory_store()     # Stores 5 in memory
calc.multiply(4)        # Result is now 20
calc.memory_recall()    # Result is now 5 (from memory)
calc.memory_add()       # Adds current result to memory (5+5=10)
calc.memory_recall()    # Result is now 10
"""

def test_calculator():
    """Run assertion tests to verify Calculator functionality."""
    # Setup
    calc = Calculator()
    
    # Test basic arithmetic
    assert calc.add(5, 3) == 8, "Addition failed"
    assert calc.subtract(10, 4) == 6, "Subtraction failed"
    assert calc.multiply(3, 4) == 12, "Multiplication failed"
    assert calc.divide(10, 2) == 5.0, "Division failed"
    
    # Test using last_result
    calc.clear()
    calc.add(10)
    assert calc.add(5) == 15, "Addition with last_result failed"
    assert calc.subtract(3) == 12, "Subtraction with last_result failed"
    assert calc.multiply(2) == 24, "Multiplication with last_result failed"
    assert calc.divide(6) == 4, "Division with last_result failed"
    
    # Test power and square root
    calc.clear()
    assert calc.add(9) == 9, "Setting value failed"
    assert calc.square_root() == 3, "Square root failed"
    assert calc.power(2) == 9, "Power operation failed"
    
    # Test memory operations
    calc.clear()
    calc.add(5)
    calc.memory_store()
    calc.clear()
    assert calc.memory_recall() == 5, "Memory recall failed"
    calc.add(3)
    calc.memory_add()
    assert calc.memory_recall() == 8, "Memory add failed"
    calc.add(2)
    calc.memory_subtract()
    assert calc.memory_recall() == 6, "Memory subtract failed"
    assert calc.memory_clear() == 0, "Memory clear failed"
    
    # Test scientific functions
    calc.clear()
    calc.add(math.pi/2)
    assert round(calc.sin(), 10) == 1.0, "Sine function failed"
    calc.clear()
    calc.add(0)
    assert calc.cos() == 1.0, "Cosine function failed"
    calc.clear()
    calc.add(100)
    assert calc.log10() == 2.0, "Log10 function failed"
    calc.clear()
    calc.add(5)
    assert calc.factorial() == 120, "Factorial function failed"
    
    # Test error handling
    calc.clear()
    try:
        calc.divide(0)
        assert False, "Division by zero should raise an error"
    except ZeroDivisionError:
        pass
    
    try:
        calc.add(-4)
        calc.square_root()
        assert False, "Square root of negative should raise an error"
    except ValueError:
        pass
    
    print("All calculator tests passed!")


# Execute the tests if this file is run directly
if __name__ == "__main__":
    test_calculator()

# Create a simple script to run.py in your project root:
from calc.gui import run

if __name__ == "__main__":
    run() 