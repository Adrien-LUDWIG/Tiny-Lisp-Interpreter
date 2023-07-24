import pytest

from lisp_evaluator import evaluate, EvaluationError


def test_number():
    assert evaluate(42) == 42


def test_not_list():
    with pytest.raises(EvaluationError) as error:
        evaluate("Not a list")
    assert (
        str(error.value)
        == "This interpreter only accepts integers and operations, for now."
    )


def test_empty_ast():
    assert evaluate([]) is None


def test_add():
    assert evaluate(["+", 23, 19]) == 42


def test_substract():
    assert evaluate(["-", 51, 9]) == 42


def test_multiply():
    assert evaluate(["*", 6, 7]) == 42


def test_unknown_operation():
    with pytest.raises(EvaluationError) as error:
        evaluate(["%", 142, 100])
    assert str(error.value).startswith("This operation doesn't exist: ")
