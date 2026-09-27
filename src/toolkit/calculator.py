from .tokenizer import tokenize
from .parser import expr

def evaluate(expression: str) -> int | float:
    return expr(tokenize(expression), 0)[0]
