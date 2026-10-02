from .tokenizer import tokenize
from .parser import expr

def evaluate(expression: str) -> int | float:
    """Extracting the answer from the given tuple"""
    try:
        return expr(tokenize(expression), 0)[0]
    except ZeroDivisionError:
        raise ValueError("You can't divide by zero.")
    except IndexError:
        raise ValueError("There's a skipped element in the expression.")
