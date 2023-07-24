import pytest

from operations.multiply import multiply


def test_no_term():
    assert multiply([]) == 1


def test_one_term():
    assert multiply([42]) == 42


def test_two_terms():
    assert multiply([6, 7]) == 42


def test_many_terms():
    assert multiply([7, 3, 2]) == 42


def test_term_not_number():
    with pytest.raises(TypeError) as error:
        multiply(["Not a number"])
    assert str(error.value).startswith(
        "Args of `*` should evaluate to `int`, but received: "
    )
