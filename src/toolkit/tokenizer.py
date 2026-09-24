def isoperator(char: str) -> bool:
    return char in ['+', '-', '*', '/', '//', '%', '**']


def read_number(s: str, i: int) -> tuple[tuple[str, int | float], int]:
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
    return (('OPERATOR', s), i + 1)

def tokenize(s: str) -> list[tuple[str, int | float | str]]:
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
