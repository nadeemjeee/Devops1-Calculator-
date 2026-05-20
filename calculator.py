class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b 
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    

if __name__ == "__main__":
    calculator = Calculator()

    print("Simple Calculator")
    print("2 + 3 =", calculator.add(2, 3))
    print("5 - 2 =", calculator.subtract(5, 2))
    print("4 * 3 =", calculator.multiply(4, 3))
    print("10 / 2 =", calculator.divide(10, 2))