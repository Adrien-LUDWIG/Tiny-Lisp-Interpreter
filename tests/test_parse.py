import pytest

from lisp_parser import _parse, ParseError


def _parse_tester(tokens, expected_ast, index=0, expected_index=None):
    if expected_index is None:
        expected_index = len(tokens)

    actual_ast, actual_index = _parse(tokens, index)

    assert actual_ast == expected_ast
    assert actual_index == expected_index


class Test_parse:
    def test_number(self):
        _parse_tester(tokens=["42"], expected_ast=42)

    def test_parentheses(self):
        _parse_tester(["(", ")"], [])

    def test_simple_operation(self):
        tokens = ["(", "+", "23", "19", ")"]
        expected_ast = ["+", 23, 19]
        _parse_tester(tokens, expected_ast)

    def test_nested_operations(self):
        tokens = ["(", "+", "23", "(", "+", "12", "7", ")", ")"]
        expected_ast = ["+", 23, ["+", 12, 7]]
        _parse_tester(tokens, expected_ast)

    def test_multi_nested_operations(self):
        tokens = [
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
        expected_ast = [
            "first",
            ["list", 1, ["+", 2, 3], ["-", 5, 4], ["*", 2, 1], ["/", 6, 3], 9],
        ]
        _parse_tester(tokens, expected_ast)

    # `_parse` should not be called with an empty list of tokens.
    def test_empty(self):
        tokens = []

        with pytest.raises(IndexError):
            _parse(tokens)

    def test_missing_parenthese(self):
        tokens = ["(", "+", "1", "2"]

        with pytest.raises(ParseError) as error:
            _parse(tokens)

        assert (
            str(error.value)
            == "Unexpected EOF. A closing parentheses `)` might be missing."
        )

    def test_unexpected_closing_parenthese(self):
        tokens = [")"]

        with pytest.raises(ParseError) as error:
            _parse(tokens)

        assert str(error.value) == "Unexpected `)`"
