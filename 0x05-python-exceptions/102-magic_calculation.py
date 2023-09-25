def magic_calculation(a, b):
    """Performs a magic calculation on a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of the magic calculation.
    """
    result = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception("Too far")
            result += (a ** b) // i
    except Exception:
        result += b + a
    return result
