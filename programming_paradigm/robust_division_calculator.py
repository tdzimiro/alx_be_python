def safe_divide(numerator, denominator):
    """Perform division with error handling for invalid inputs and division by zero."""

    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

