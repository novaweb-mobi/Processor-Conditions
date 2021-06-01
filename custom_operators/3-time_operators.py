def add_operators(self):
    return {'before_time': time_before,
            'equal_time': time_equal,
            'after_time': time_after}


def time_before(value: datetime, reference: datetime) -> bool:
    return less_than(value.hour, reference.hour) \
        or (eql(value.hour, reference.hour)
            and less_than(value.minute, reference.minute))


def time_equal(value: datetime, reference: datetime) -> bool:
    return eql(value.hour, reference.hour) \
        and eql(value.minute, reference.minute)


def time_after(value: datetime, reference: datetime) -> bool:
    return not time_before(value, reference) \
        and not time_equal(value, reference)
