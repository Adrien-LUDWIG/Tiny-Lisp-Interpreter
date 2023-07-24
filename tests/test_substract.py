import pytest

from operations.substract import substract


def test_no_term():
    with pytest.raises(ValueError) as error:
        substract([]) == 0
    assert str(error.value) == "`-` takes one or more term(s)."


def test_one_term():
    assert substract([42]) == -42


def test_two_terms():
    assert substract([51, 9]) == 42


def test_many_terms():
    assert (
        substract(
            [
                51,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ]
        )
        == 42
    )


def test_first_term_not_number():
    with pytest.raises(TypeError) as error:
        substract(["Not a number"])
    assert str(error.value).startswith(
        "Args of `-` should evaluate to `int`, but received: "
    )


def test_following_term_not_number():
    with pytest.raises(TypeError) as error:
        substract([42, "Not a number"])
    assert str(error.value).startswith(
        "Args of `-` should evaluate to `int`, but received: "
    )
