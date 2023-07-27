from operations.operation_argument_error import OperationArgumentError


def multiply(terms):
    product = 1

    for term in terms:
        if type(term) != int:
            raise OperationArgumentError(
                "Args of `*` should evaluate to `int`, but received: " + str(term)
            )

        product *= term

    return product
