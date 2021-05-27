def add_operators(self):
    return {'contain': contains,
            'not_contain': not_contains}


def contains(value: Iterable, reference: Any) -> bool:
    try:
        return reference in value
    except TypeError:
        return False


def not_contains(value: Iterable, reference: Any) -> bool:
    return not contains(value, reference)
