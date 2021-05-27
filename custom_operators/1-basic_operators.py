def add_operators(self):
    return {'==': eql,
            '!=': different,
            '>': greater_than,
            '<': less_than,
            '>=': greater_or_equal_than,
            '<=': less_or_equal_than}


def eql(value: Any, reference: Any) -> bool:
    return value == reference


def different(value: Any, reference: Any) -> bool:
    return not eql(value, reference)


def greater_than(value: Any, reference: Any) -> bool:
    return value > reference


def less_than(value: Any, reference: Any) -> bool:
    return value < reference


def greater_or_equal_than(value: Any, reference: Any) -> bool:
    return value >= reference


def less_or_equal_than(value: Any, reference: Any) -> bool:
    return value <= reference
