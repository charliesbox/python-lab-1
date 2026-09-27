import argparse
import sys
from .calculator import evaluate


parser = argparse.ArgumentParser(description='CLI Toolkit')
subparsers = parser.add_subparsers(dest='command')

calc_parser = subparsers.add_parser('calc', help='Calculate a math expression')
calc_parser.add_argument('expression', type=str, help='The expression to calculate')


args = parser.parse_args()

if args.command == 'calc':
    if args.expression == '':
        print('Empty expression given.')
        sys.exit(2)
    try:
        result = evaluate(args.expression)
        print(result)
    except ValueError as e:
        print(f'{e}', file=sys.stderr)
        sys.exit(2)
    except ZeroDivisionError:
        print("You can't divide by zero.")
        sys.exit(2)
    except IndexError:
        print("There's a skipped element in the expression.")
        sys.exit(2)
