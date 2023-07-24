import pytest

from operations.add import add


def test_no_term():
    assert add([]) == 0


def test_one_term():
    assert add([42]) == 42


def test_two_terms():
    assert add([23, 19]) == 42


def test_many_terms():
    assert (
        add(
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
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


def test_term_not_number():
    with pytest.raises(TypeError) as error:
        add(["Not a number"])
    assert str(error.value).startswith(
        "Args of `+` should evaluate to `int`, but received: "
    )
