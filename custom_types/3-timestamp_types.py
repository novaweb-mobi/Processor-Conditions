from datetime import datetime

from dictor import dictor


def add_types(self):
    return {'timestamp': timestamp_processor}


def timestamp_processor(body: dict, condition: dict) -> bool:
    value = dictor(body, 'event.content.timestamp')

    operator = __get_operator_or_default(condition.get("operator"))

    return operator(value,
                    datetime.strptime(condition.get('value'),
                                      "%Y-%m-%dT%H:%M:%S.%fZ"))
