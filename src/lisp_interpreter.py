from lisp_evaluator import evaluate, EvaluationError
from lisp_parser import parse, ParseError
from lisp_tokenizer import tokenize
from operations.operation_argument_error import OperationArgumentError


def run(source_code):
    tokens = tokenize(source_code)
    asts = parse(tokens)
    return evaluate(asts)


def REPL():
    try:
        while True:
            source_code = input(">>> ")

            try:
                result = run(source_code)

                if result is not None:
                    print(result)

            except (ParseError, EvaluationError, OperationArgumentError) as error:
                print(error)

    except KeyboardInterrupt:
        print("\nBye!")
