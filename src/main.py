from argparse import ArgumentParser
from pathlib import Path

from lisp_evaluator import _evaluate
from lisp_parser import parse
from lisp_tokenizer import tokenize


class ArgumentError(ValueError):
    pass


def parse_args():
    parser = ArgumentParser(
        prog="tiny-lisp-interpreter",
        description="A tiny Lisp interpreter in Python 🐍",
        epilog="Without argument, the program starts in interactive mode (REPL).",
    )
    parser.add_argument(
        "file",
        nargs="?",
        default=None,
        type=Path,
        help="Program read from script file. Mutually exclusive with `--command`.",
    )
    parser.add_argument(
        "-c",
        "--command",
        default=None,
        type=str,
        help="Program passed in as a string. Mutually exclusive with `file`.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.file is not None and args.command is not None:
        raise ArgumentError("`file` and `--command` arguments are mutually exclusive.")

    if args.file is not None:
        with open(args.file, "r") as file:
            return _evaluate(parse(tokenize(file.read())))

    if args.command is not None:
        return _evaluate(parse(tokenize(args.command)))

    print("REPL")


if __name__ == "__main__":
    print(main())
