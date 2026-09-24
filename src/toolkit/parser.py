def isoperator(char: str) -> bool:
    return char in ['+', '-', '*', '/', '//', '%', '**']

def factor(tokens: list[tuple[str, int | float | str]], i: int):
    if tokens[i][1] == '-':
        new_value, i = factor(tokens, i + 1)
        inverted_value = new_value * (-1)
        return (inverted_value, i)

    elif tokens[i][1] == '(':
        new_value, i = expr(tokens, i + 1)
        if i >= len(tokens):
            raise ValueError("You haven't closed the parenthesis.")
        return (new_value, i + 1)

    else:
        return (tokens[i][1], i + 1)

def term(tokens, i):
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
