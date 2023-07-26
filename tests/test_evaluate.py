import pytest

from lisp_evaluator import _evaluate, EvaluationError


def test_number():
    assert _evaluate(42) == 42


def test_not_list():
    with pytest.raises(EvaluationError) as error:
        _evaluate("Not a list")
    assert (
        str(error.value)
        == "This interpreter only accepts integers and operations, for now."
    )


def test_empty_ast():
    assert _evaluate([]) is None


def test_add():
    assert _evaluate(["+", 23, 19]) == 42


def test_substract():
    assert _evaluate(["-", 51, 9]) == 42


def test_multiply():
    assert _evaluate(["*", 6, 7]) == 42


def test_unknown_operation():
    with pytest.raises(EvaluationError) as error:
        _evaluate(["%", 142, 100])
    assert str(error.value).startswith("This operation doesn't exist: ")
