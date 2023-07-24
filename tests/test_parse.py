import pytest

from lisp_parser import parse, ParseError


def test_number():
    assert parse(["42"]) == 42


def test_parentheses():
    assert parse(["(", ")"]) == []


def test_simple_operation():
    assert parse(["(", "+", "23", "19", ")"]) == ["+", 23, 19]


def test_nested_operations():
    actual = parse(["(", "+", "23", "(", "+", "12", "7", ")", ")"])
    excepted = ["+", 23, ["+", 12, 7]]
    assert actual == excepted


def test_multi_nested_operations():
    assert parse(
        [
            "(",
            "first",
            "(",
            "list",
            "1",
            "(",
            "+",
            "2",
            "3",
            ")",
            "(",
            "-",
            "5",
            "4",
            ")",
            "(",
            "*",
            "2",
            "1",
            ")",
            "(",
            "/",
            "6",
            "3",
            ")",
            "9",
            ")",
            ")",
        ]
    ) == ["first", ["list", 1, ["+", 2, 3], ["-", 5, 4], ["*", 2, 1], ["/", 6, 3], 9]]


def test_empty():
    assert parse([]) == []


def test_missing_parenthese():
    with pytest.raises(ParseError) as error:
        parse(["(", "+", "1", "2"])

    assert (
        str(error.value)
        == "Unexpected EOF. A closing parentheses `)` might be missing."
    )


def test_unexpected_closing_parenthese():
    with pytest.raises(ParseError) as error:
        parse([")"])

    assert str(error.value) == "Unexpected `)`"


def test_unreachable_tokens():
    with pytest.raises(ParseError) as error:
        parse(["(", "+", "1", "2", ")", "3"])

    assert str(error.value) == "You have unreachable code."
