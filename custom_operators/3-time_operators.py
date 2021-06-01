from datetime import datetime


def add_operators(self):
    return {'before_time': {
        'operation': time_before,
        'descriptions': {
            'time': {
                'pt': 'Antes da hora',
                'en': 'Before hour'
            }
        }
    },
        'equal_time': {
            'operation': time_equal,
            'descriptions': {
                'time': {
                    'pt': 'Na hora',
                    'en': 'At hour'
                }
            }
        },
        'after_time': {
            'operation': time_after,
            'descriptions': {
                'time': {
                    'pt': 'Depois da hora',
                    'en': 'After hour'
                }
            }
        }
    }


def time_before(value: datetime, reference: datetime) -> bool:
    return value.hour < reference.hour \
           or (value.hour == reference.hour
               and value.minute < reference.minute)


def time_equal(value: datetime, reference: datetime) -> bool:
    return value.hour == reference.hour \
           and value.minute == reference.minute


def time_after(value: datetime, reference: datetime) -> bool:
    return not time_before(value, reference) \
           and not time_equal(value, reference)
