# CLI Toolkit

## Project Description

`toolkit` is a CLI utility with two commands:
- `calc` - evaluates arithmetic expressions (`+ - * /`, parentheses, unary `+`/`-`), implemented via a custom tokenizer and a recursive descent parser, without using `eval`/`exec`/`ast.literal_eval`.
- `convert` - converts units of measurement: length (mm/cm/m/km), mass (g/kg), temperature (c/f/k). Units are case-insensitive. Note that the converter rounds values to 4 digits after the decimal point.
- `help` - prints the list of commands along with explanations for them.

## Idea and Infrastructure
The goal of the project is to show how to evaluate math expressions without the built-in python tools like `eval()` and build our own calculator instead. Additionally, we learn how to work with such python libraries as `pytest` and `argparse`.

## Project Structure
```
src/toolkit/
    __init__.py
    __main__.py    — entry point, argparse CLI
    tokenizer.py    — string → tokens
    parser.py       — recursive descent parser
    calculator.py   — evaluate(): combines tokenizer + parser
    converter.py    — convert(): unit conversion logic
    constants.py    — unit coefficient tables
tests/
    test_calculator.py
    test_converter.py
```

### Calculator
The calculator evaluates a given string with a math expression and returns the answer.
The pipeline looks like this:
```
'2 * (3 + 5)'
    |
    ▼
tokenizer.py
Turns a string into a list of tokens.
(('NUMBER', 2), ('OPERATOR', '*'), ...)
    |
    ▼
parser.py
Calculates the expression, respective to the * and / over + and - priority.
Uses the recursive descent method to evaluate.
    |
    ▼
calculator.py
The entry point of the calculator module. Returns a digit, which is the answer.
    |
    ▼
__main__.py
The entry point of the entire CLI toolkit. Prints the answer or catches ValueErrors raised by previous modules.
```

### Help file
The `help.py` file contains the text of `help` command.

### Converter
The converter turns a value from one measurement unit to another one.
The supported units are `kg, g` for weight, `mm, cm, m, km` for length, `c, f, k` for temperature.
The measurement units' coefficients are stored at `constants.py`. The given unit is first converted into a common unit (e.g. kg, m, or Kelvin) and then is converted into the desired unit.
The temperature is processed separately because of the complex formula for the Fahrenheit unit.

### Error handling
None of the modules just `sys.exit()` with an error thrown into the console mindlessly in case of exceptions. Instead, they `raise` a ValueError that is then caught by `__main__.py` and printed for the user, and then the program is closed with an exit code of `2`. For example, in `calculator.py`:
```python
try:
    return expr(tokenize(expression), 0)[0]
except ZeroDivisionError:
    raise ValueError("You can't divide by zero.")
```
...and then, in `__main__.py`:
```python
try:
    calc_result = evaluate(args.expression)
    print(calc_result)
except ValueError as e:
    print(f'{e}', file=sys.stderr)
    sys.exit(2)
```

### Rounding
The converter features rounding the answer up to 4 digits after the dot. This can be changed by editing the `PRECISION` variable in `converter.py`. The calculator doesn't feature any rounding.

## Testing
19 pytest tests (11 for `calc`, 8 for `convert`) covering both successful scenarios and all error cases listed above.

```bash
uv run pytest -v
```

## Installation and Usage

### Clone the repository to your machine
```bash
git clone https://github.com/charliesbox/python-lab-1
```

### Set up the virtual environment and dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage
To use the tool, navigate to the `src` directory located in the project root.
```bash
cd src
```
Done! You can now use it:
```bash
python -m toolkit calc "2 + 3 * 4"
python -m toolkit convert 17.3 --from c --to k
```
