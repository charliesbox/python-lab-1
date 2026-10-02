def isoperator(char: str) -> bool:
    """Checks if the next character is an opeartor"""
    return char in ['+', '-', '*', '/', '//', '%', '**']


def read_number(s: str, i: int) -> tuple[tuple[str, int | float], int]:
    """Turning a number into a tokenL a tuple that contains the info about the fact
    it's a number and the number itself"""
    number = ''
    fraction = False

    while True:
        if i >= len(s):
            break

        elif s[i].isdigit():
            number += s[i]

        elif s[i] == '.' and not fraction:
            number += s[i]
            fraction = True

        elif s[i] == '.' and fraction:
            raise ValueError('Invalind element in the expression.')

        else:
            break

        i += 1

    if fraction:
        return (('NUMBER', float(number)), i)
    else:
        return (('NUMBER', int(number)), i)


def read_operator(s: str, i: int) -> tuple[tuple[str, str], int]:
    """Turn an operator into a token"""
    return (('OPERATOR', s), i + 1)

def tokenize(s: str) -> list[tuple[str, int | float | str]]:
    """The entry point of the tokenizer. Turns the given string into a tuple of tokens"""

    tokens: list[tuple[str, int | float | str]] = []
    token: tuple[str, int | float | str]
    i = 0
    while i < len(s):
        if s[i].isdigit() or s[i] == '.':
            token, i = read_number(s, i)
            tokens.append(token)
            continue

        elif isoperator(s[i]):
            token, i = read_operator(s[i], i)
            tokens.append(token)
            continue

        elif s[i] == ' ':
            i += 1
            continue

        elif s[i] == '(':
            token, i = read_operator(s[i], i)
            tokens.append(token)
            continue

        elif s[i] == ')':
            token, i = read_operator(s[i], i)
            tokens.append(token)
            continue

        else:
            raise ValueError('Invalid symbol in the expression.')
    return tokens
