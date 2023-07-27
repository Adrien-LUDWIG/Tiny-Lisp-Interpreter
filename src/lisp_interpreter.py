from lisp_evaluator import evaluate
from lisp_parser import parse
from lisp_tokenizer import tokenize


def run(source_code):
    tokens = tokenize(source_code)
    asts = parse(tokens)
    return evaluate(asts)
