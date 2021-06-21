from typing import Any, Iterable


def add_operators():
    return {'contain': {
        'operation': contains,
        'descriptions': {
            'string': {
                'pt': 'Contém',
                'en': 'Contains'
            },
            'array': {
                'pt': 'Contém',
                'en': 'Contains'
            },
            'object': {
                'pt': 'Possui a propriedade',
                'en': 'Has property'
            }
        }
    },
        'not_contain': {
            'operation': not_contains,
            'descriptions': {
                'string': {
                    'pt': 'Não contém',
                    'en': 'Doesn\'t contain'
                },
                'array': {
                    'pt': 'Não contém',
                    'en': 'Doesn\'t contain'
                },
                'object': {
                    'pt': 'Não possui a propriedade',
                    'en': 'Doesn\'t have property'
                }
            }
    }
    }


def contains(value: Iterable, reference: Any) -> bool:
    try:
        return reference in value
    except TypeError:
        return False


def not_contains(value: Iterable, reference: Any) -> bool:
    return not contains(value, reference)
