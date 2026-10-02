# CLI Toolkit

## Project Description

`toolkit` is a CLI utility with two commands:
- `calc` - evaluates arithmetic expressions (`+ - * /`, parentheses, unary `+`/`-`), implemented via a custom tokenizer and a recursive descent parser, without using `eval`/`exec`/`ast.literal_eval`.
- `convert` - converts units of measurement: length (mm/cm/m/km), mass (g/kg), temperature (c/f/k). Units are case-insensitive. Note that the converter rounds values to 4 digits after the decimal point.
- `help` - prints the list of commands along with explanations for them.

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
python -m toolkit convert ```
