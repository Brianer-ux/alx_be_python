# robust_division_calculator.py
"""Performs division safely, handling invalid input and division by zero."""

def safe_divide(numerator, denominator):
    """
    Divide two values safely with error handling.

    Parameters:
        numerator: can be string or number
        denominator: can be string or number

    Returns:
        str: Message with either the result or an error description.
    """
    try:
        # Try converting inputs to floats (will raise ValueError if not numbers)
        num = float(numerator)
        den = float(denominator)

        # Try performing the division (may raise ZeroDivisionError)
        result = num / den

        return f"The result of the division is {result}"

    except ValueError:
        # This happens when conversion to float fails
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Happens when denominator == 0
        return "Error: Cannot divide by zero."
