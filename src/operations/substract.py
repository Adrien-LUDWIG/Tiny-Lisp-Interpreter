from operations.operation_argument_error import OperationArgumentError


def substract(terms):
    if terms == []:
        raise OperationArgumentError("`-` takes one or more term(s).")

    first_value = terms.pop(0)

    if type(first_value) != int:
        raise OperationArgumentError(
            "Args of `-` should evaluate to `int`, but received: " + str(first_value)
        )

    if terms == []:
        return -first_value

    difference = first_value

    for term in terms:
        if type(term) != int:
            raise OperationArgumentError(
                "Args of `-` should evaluate to `int`, but received: "
                + str(first_value)
            )

        difference -= term

    return difference
