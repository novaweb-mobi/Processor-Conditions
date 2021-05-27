def add_types(self):
    return {'entry_model': entry_model_processor}


def entry_model_processor(body: dict, condition: dict) -> bool:
    assert isinstance(body, dict)
    value = dictor(body, '.'.join(
        ['event.content.content', condition.get('property', '')]))

    operator = __get_operator_or_default(condition.get("operator"))

    return operator(value, condition.get('value'))
