from sympy import sympify, sqrt
import re


def evaluate_expression(expression, precision=10):
    try:
        # Convert percentage to a decimal
        expression = re.sub(r'(\d+)%', r'(\1/100)', expression)

        # Define a custom function for sqr
        def sqr(x):
            return x ** 2

        # Replace sqr() with the custom sqr function
        expression = re.sub(r'sqr\((.*?)\)', r'sqr(\1)', expression)

        # Evaluate the expression using sympy
        result = sympify(expression, {'sqr': sqr}).evalf()

        # Format the result to a string with specified precision
        result_str = format(result, f'.{precision}f').rstrip('0').rstrip('.')

        return result_str
    except Exception as e:
        return "Error"

