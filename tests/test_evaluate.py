import pytest

from lisp_evaluator import _evaluate, EvaluationError, evaluate


class Test_evaluate:
    def test_number(self):
        assert _evaluate(42) == 42

    def test_not_list(self):
        with pytest.raises(EvaluationError) as error:
            _evaluate("Not a list")
        assert (
            str(error.value)
            == "This interpreter only accepts integers and operations, for now."
        )

    def test_empty_ast(self):
        assert _evaluate([]) is None

    def test_add(self):
        assert _evaluate(["+", 23, 19]) == 42

    def test_substract(self):
        assert _evaluate(["-", 51, 9]) == 42

    def test_multiply(self):
        assert _evaluate(["*", 6, 7]) == 42

    def test_unknown_operation(self):
        with pytest.raises(EvaluationError) as error:
            _evaluate(["%", 142, 100])
        assert str(error.value).startswith("This operation doesn't exist: ")


class TestEvaluate:
    def test_no_ast(self):
        assert evaluate([]) is None

    def test_multi_asts(self):
        assert evaluate([["-", 23, 19], 42]) == 42
