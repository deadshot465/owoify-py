def interleave_arrays(a: list, b: list) -> list:
    arr = []
    observed = a
    other = b
    temp = []

    while len(observed) > 0:
        arr.append(observed.pop(0))
        temp = observed
        observed = other
        other = temp

    if len(other) > 0:
        arr += other
    return arr
