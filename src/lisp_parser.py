class ParseError(ValueError):
    pass


def _parse(tokens, index=0):
    token = tokens[index]

    if token == ")":
        raise ParseError("Unexpected `)`")
    elif token == "(":
        expression = []

        index += 1
        while index < len(tokens) and tokens[index] != ")":
            sub_expression, index = _parse(tokens, index)
            expression.append(sub_expression)

        if index == len(tokens):
            raise ParseError(
                "Unexpected EOF. A closing parentheses `)` might be missing."
            )

        return expression, index + 1
    elif token.isdigit():
        return int(token), index + 1
    else:
        return token, index + 1


def parse(tokens):
    # Empty input
    if len(tokens) == 0:
        return []

    ast, index = _parse(tokens, index=0)

    if index != len(tokens):
        raise ParseError("You have unreachable code.")

    return ast
