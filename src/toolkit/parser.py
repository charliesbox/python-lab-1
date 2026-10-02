"""
             CAUTION
    NOW ENTERING IF-ELFE FOREST
ABANDON ALL HOPE ALL YE WHO ENTER HERE
"""

def isoperator(char: str) -> bool:
    """Check if the given character is an operator. """
    return char in ['+', '-', '*', '/', '//', '%', '**']

def factor(tokens: list[tuple[str, int | float | str]], i: int):
    """Brings the next token to the function that called it"""

    if tokens[i][1] == '-':
        new_value, i = factor(tokens, i + 1)
        inverted_value = new_value * (-1)
        return (inverted_value, i)

    if tokens[i][1] == '+':
        new_value, i = factor(tokens, i + 1)
        return (new_value, i)

    elif tokens[i][1] == '(':
        new_value, i = expr(tokens, i + 1)
        if i >= len(tokens):
            raise ValueError("You haven't closed the brackets.")
        return (new_value, i + 1)

    else:
        if tokens[i][0] == 'NUMBER':
            return (tokens[i][1], i + 1)
        raise ValueError("Got two operators in a row.")

def term(tokens, i):
    """Calculates * and / logic"""

    value, i = factor(tokens, i)

    while i < len(tokens) and tokens[i][1] in ['*', '/']:
        operator = tokens[i][1]
        i += 1
        next_value, i = factor(tokens, i)

        if operator == '*':
            value = value * next_value
        elif operator == '/':
            value = value / next_value

    return (value, i)

def expr(tokens, i):
    """The entry point of the parser: calculates + and -, respecting the * and / priority with term()"""

    value, i = term(tokens, i)

    while i < len(tokens) and tokens[i][1] in ['+', '-']:
        operator = tokens[i][1]
        i += 1
        next_value, i = term(tokens, i)

        if operator == '+':
            value = value + next_value
            continue
        elif operator == '-':
            value = value - next_value
            continue

    return (value, i)
