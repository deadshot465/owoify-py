import collections.abc


def flatten(arr: collections.abc.Iterable):
    """
    Flatten the iterable collection. Modified from: https://note.nkmk.me/en/python-list-flatten/
    :param arr: The iterable collection to flatten
    :return: The generator of the flattened collection.
    """
    for elem in arr:
        if isinstance(elem, collections.abc.Iterable) and not isinstance(elem, (str, bytes)):
            yield from flatten(elem)
        else:
            yield elem
