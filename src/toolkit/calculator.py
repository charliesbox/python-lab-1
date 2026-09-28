import sys
from .tokenizer import tokenize
from .parser import expr

def evaluate(expression: str) -> int | float:
    try:
        return expr(tokenize(expression), 0)[0]
    except ZeroDivisionError:
        print("You can't divide by zero.")
        sys.exit(2)
    except IndexError:
        print("There's a skipped element in the expression.")
        sys.exit(2)
