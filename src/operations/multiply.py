def multiply(terms):
    product = 1

    for term in terms:
        if type(term) != int:
            raise TypeError(
                "Args of `*` should evaluate to `int`, but received: " + str(term)
            )

        product *= term

    return product
