from operations.add import add
from operations.substract import substract
from operations.multiply import multiply


class EvaluationError(ValueError):
    pass


def _evaluate(ast):
    # Atom: integer
    if type(ast) is int:
        return ast

    if type(ast) is not list:
        raise EvaluationError(
            "This interpreter only accepts integers and operations, for now."
        )

    if ast == []:
        return None

    operation = ast.pop(0)
    terms = [_evaluate(expression) for expression in ast]

    match operation:
        case "+":
            return add(terms)
        case "-":
            return substract(terms)
        case "*":
            return multiply(terms)

    raise EvaluationError("This operation doesn't exist: " + str(operation))
