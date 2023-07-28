# Tiny-Lisp-Interpreter

A tiny Lisp interpreter in Python! 🐍

## Features 🎉

- Tokenizer, parser and evaluator
- Input as REPL, file or command
- Operations: `+`, `-`, `*` *(for now)*
- Positive integers only *(for now)*
- Error detection
- No dependencies

See [TODO.md](./TODO.md) for the next features I want to add.

## Repository structure 📁

```sh
.
├── experiments
│   └── lisp-interpreter.ipynb # Notebook containing my first experiments
├── README.md
├── src
│   ├── lisp_evaluator.py
│   ├── lisp_interpreter.py # Contains the REPL
│   ├── lisp_parser.py
│   ├── lisp_tokenizer.py
│   ├── main.py # Entry point of the program
│   └── operations # Add, sub, mul, div, etc.
│       └── ...
├── tests
│   └── ...
└── TODO.md # Some features I want to add
```

## Installation

```sh
git clone git@github.com:Adrien-LUDWIG/Tiny-Lisp-Interpreter.git
cd Tiny-Lisp-Interpreter
# And nothing else! There is no dependencies! (unless you want to run the tests)
```

## Usage

To show the help:

```sh
python src/main.py --help
```

To start the REPL:

```sh
python src/main.py
```

To run a file:

```sh
python src/main.py ./path/to/file.lisp
```

To run a command:

```sh
python src/main.py --command "(+ 23 19)"
```

## Examples 📝

This Tiny List Interpreter can currently run this:

```lisp
(+ 23 19)
(- 51 9)
(* 7 3 2)
(- (+ 31 7 13) (* 3 3))
```

## Development 🛠

### Requirements 📦

- pytest

### Tests 🧪

To run the tests:

```sh
pytest
```

## Tools 🔧

[![Python](https://img.shields.io/badge/Python-3776AB?logo=Python&logoColor=white&style=for-the-badge)](https://en.wikipedia.org/wiki/Python_(programming_language))
[![Pytest](https://img.shields.io/badge/Pytest-3776AB?logo=Pytest&logoColor=white&style=for-the-badge)](https://en.wikipedia.org/wiki/Pytest)
