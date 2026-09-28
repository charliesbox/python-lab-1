import argparse
import sys
from .calculator import evaluate
from .converter import convert

def main() -> None:
    parser = argparse.ArgumentParser(description='CLI Toolkit')
    subparsers = parser.add_subparsers(dest='command')

    calc_parser = subparsers.add_parser('calc', help='Calculate a math expression')
    calc_parser.add_argument('expression', type=str, help='The expression to calculate')

    convert_parser = subparsers.add_parser('convert', help='Convert different measurement units')
    convert_parser.add_argument('value', type=str, help='The original value')
    convert_parser.add_argument('--from', dest='unit_from', type=str, required=True)
    convert_parser.add_argument('--to', type=str, dest='unit_to', required=True)

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


    if args.command == 'convert':
        try:
            result = convert(args.value, args.unit_from, args.unit_to)
            print(f'{result} {args.unit_to}')
            sys.exit(0)
        except ValueError as e:
            print(f'{e}', file=sys.stderr)
            sys.exit(2)

if __name__ == '__main__':
    main()
