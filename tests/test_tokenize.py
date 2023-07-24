from tokenizer import tokenize


def test_number():
    assert tokenize("42") == ["42"]


def test_parentheses():
    assert tokenize("()") == ["(", ")"]


def test_simple_operation():
    assert tokenize("(+ 23 19)") == ["(", "+", "23", "19", ")"]


def test_nested_operations():
    actual = tokenize("(+ 23 (+ 12 7))")
    excepted = ["(", "+", "23", "(", "+", "12", "7", ")", ")"]
    assert actual == excepted


def test_multi_nested_operations():
    assert tokenize("(first (list 1 (+ 2 3) (- 5 4) (* 2 1) (/ 6 3) 9))") == [
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
