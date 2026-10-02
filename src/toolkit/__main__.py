import argparse
import sys
from .calculator import evaluate
from .converter import convert
from .help import help

def main() -> None:
    """Parsing arguments and executing user's commands"""

    parser = argparse.ArgumentParser(description='CLI Toolkit')
    subparsers = parser.add_subparsers(dest='command')

    calc_parser = subparsers.add_parser('calc', help='Calculate a math expression')
    calc_parser.add_argument('expression', type=str, help='The expression to calculate')

    convert_parser = subparsers.add_parser('convert', help='Convert different measurement units')
    convert_parser.add_argument('value', type=str, help='The original value')
    convert_parser.add_argument('--from', dest='unit_from', type=str, required=True)
    convert_parser.add_argument('--to', type=str, dest='unit_to', required=True)

    subparsers.add_parser('help', help='Print command list')
    args = parser.parse_args()

    if args.command == 'calc':
        if args.expression == '':
            print('Empty expression given.')
            sys.exit(2)
        try:
            calc_result = evaluate(args.expression)
            print(calc_result)
        except ValueError as e:
            print(f'{e}', file=sys.stderr)
            sys.exit(2)


    if args.command == 'convert':
        try:
            convert_result = convert(args.value, args.unit_from, args.unit_to)
            print(f'{convert_result} {args.unit_to}')
            sys.exit(0)
        except ValueError as e:
            print(f'{e}', file=sys.stderr)
            sys.exit(2)

    if args.command == 'help' or args.command is None:
        print(help())
        sys.exit(0)

if __name__ == '__main__':
    main()
