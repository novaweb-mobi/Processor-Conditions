from typing import Union


def add_operators():
    return {'==': {
        'operation': eql,
        'descriptions': {
            'string': {
                'pt': 'É igual à',
                'en': 'Is'
            },
            'number': {
                'pt': 'É igual à',
                'en': 'Is equal to'
            },
            'array': {
                'pt': 'Contém apenas',
                'en': 'Contains only'
            },
            'object': {
                'pt': 'É',
                'en': 'Is'
            },
            'bool': {
                'pt': 'É',
                'en': 'Is'
            },
            'datetime': {
                'pt': 'Data e hora é',
                'en': 'Date and time are'
            }
        }
    },
        '!=': {
            'operation': different,
            'descriptions': {
                'string': {
                    'pt': 'Não é igual à',
                    'en': 'Is not'
                },
                'number': {
                    'pt': 'Não é igual à',
                    'en': 'Is not equal to'
                },
                'array': {
                    'pt': 'Não é',
                    'en': 'Is not'
                },
                'object': {
                    'pt': 'Não é',
                    'en': 'Is not'
                },
                'bool': {
                    'pt': 'Não é',
                    'en': 'Is not'
                },
                'datetime': {
                    'pt': 'Data e hora não é',
                    'en': 'Date and time aren\'t'
                }
            }
        },
        '>': {
            'operation': greater_than,
            'descriptions': {
                'string': {
                    'pt': 'É maior que (ordem alfabética)',
                    'en': 'Is greater than (Alphabetical order)'
                },
                'number': {
                    'pt': 'É maior que',
                    'en': 'Is greater than'
                },
                'datetime': {
                    'pt': 'Depois de',
                    'en': 'After'
                }
            }
        },
        '<': {
            'operation': less_than,
            'descriptions': {
                'string': {
                    'pt': 'É menor que (ordem alfabética)',
                    'en': 'Is less than (Alphabetical order)'
                },
                'number': {
                    'pt': 'É menor que',
                    'en': 'Is less than'
                },
                'datetime': {
                    'pt': 'Antes de',
                    'en': 'Before'
                }
            }
        },
        '>=': {
            'operation': greater_or_equal_than,
            'descriptions': {
                'string': {
                    'pt': 'É maior que ou igual à (ordem alfabética)',
                    'en': 'Is greater than or equal to (Alphabetical order)'
                },
                'number': {
                    'pt': 'É maior que ou igual à',
                    'en': 'Is greater than or equal to'
                },
                'datetime': {
                    'pt': 'Depois de ou em',
                    'en': 'After or on'
                }
            }
        },
        '<=': {
            'operation': less_or_equal_than,
            'descriptions': {
                'string': {
                    'pt': 'É menor que ou igual à (ordem alfabética)',
                    'en': 'Is less than or equal to (Alphabetical order)'
                },
                'number': {
                    'pt': 'É menor que ou igual à',
                    'en': 'Is less than or equal to'
                },
                'datetime': {
                    'pt': 'Antes de ou em',
                    'en': 'Before or on'
                }
            }
        }
    }


def eql(value: Union[str, int, float, list, dict, bool],
        reference: Union[str, int, float, list, dict, bool]) -> bool:
    return value == reference


def different(value: Union[str, int, float, list, dict, bool],
              reference: Union[str, int, float, list, dict, bool]) -> bool:
    return not eql(value, reference)


def greater_than(value: Union[str, int, float],
                 reference: Union[str, int, float]) -> bool:
    return value > reference


def less_than(value: Union[str, int, float],
              reference: Union[str, int, float]) -> bool:
    return value < reference


def greater_or_equal_than(value: Union[str, int, float],
                          reference: Union[str, int, float]) -> bool:
    return value >= reference


def less_or_equal_than(value: Union[str, int, float],
                       reference: Union[str, int, float]) -> bool:
    return value <= reference
