def substract(terms):
    if terms == []:
        raise ValueError("`-` takes one or more term(s).")

    first_value = terms.pop(0)

    if type(first_value) != int:
        raise TypeError(
            "Args of `-` should evaluate to `int`, but received: " + str(first_value)
        )

    if terms == []:
        return -first_value

    difference = first_value

    for term in terms:
        if type(term) != int:
            raise TypeError(
                "Args of `-` should evaluate to `int`, but received: "
                + str(first_value)
            )

        difference -= term

    return difference
