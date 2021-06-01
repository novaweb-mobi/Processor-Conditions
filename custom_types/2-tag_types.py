from dictor import dictor


def add_types(self):
    return {'tag': tag_processor}


def tag_processor(body: dict, condition: dict) -> bool:
    values = dictor(body,
                    f'event.content.tags.{condition.get("property")}',
                    [])

    operator = __get_operator_or_default(condition.get("operator"), "contain")

    return operator(values, condition.get('value'))
