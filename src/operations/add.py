def add(terms):
    sum = 0

    for term in terms:
        if type(term) != int:
            raise TypeError(
                "Args of `+` should evaluate to `int`, but received: " + str(term)
            )

        sum += term

    return sum
