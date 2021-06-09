from dictor import dictor


def add_types():
    return {'timeline': timeline_processor}


def timeline_processor(body: dict, condition: dict) -> bool:
    values = dictor(body, 'event.content.timelines', [])

    operator = __get_operator_or_default(condition.get("operator"), "contain")

    return operator(values, condition.get('value'))
