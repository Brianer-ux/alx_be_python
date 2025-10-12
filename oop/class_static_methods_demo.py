# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Adds two numbers. Does not need class or instance access.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Multiplies two numbers. Can access class attributes via cls.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
