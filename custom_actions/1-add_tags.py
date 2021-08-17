from typing import Set

from dictor import dictor

from utils import EventContent, GUID


def add_actions():
    return {
        "add_tags": {
            "operation": add_tags,
            "name": "Adicionar tags",
            "data_fields": [
                {
                    "key": "tags",
                    "label": "Tag",
                    "field_type": "object",
                    "field_options": {
                        "property_key": {
                            "label": "Tag",
                            "field_type": "select",
                            "field_options": {
                                "from": {
                                    "url": "https://smartview-api.novaweb.duckdns.org:16443/v1/tag/",
                                    "optionsPath": "data.results",
                                    "label": "identifier",
                                    "value": "id_"
                                }
                            }
                        },
                        "property_value": {
                            "label": "Valor",
                            "field_type": "select",
                            "field_options": {
                                "from": {
                                    "url": "https://smartview-api.novaweb.duckdns.org:16443/v1/tag/{{"
                                           "property_key}}/value",
                                    "optionsPath": "data.results",
                                    "label": "value",
                                    "value": "id_"
                                }
                            }
                        }
                    }
                }
            ]
        }
    }


def add_tags(event_content: EventContent, data: dict):
    tags: dict = data.get('tags')
    for tag_id_, values in tags.items():
        tag_value_set = __get_event_tag_list(event_content, tag_id_)

        for value_id_ in values:
            tag_value_set.add(value_id_)

        event_content['event']['content']['tags'][tag_id_] \
            = list(tag_value_set)

    return event_content


def __get_event_tag_list(event_content: EventContent,
                         tag_id_: GUID) -> Set[GUID]:
    tag_list = dictor(event_content, f'event.content.tags.{tag_id_}') \
               or list()
    return set(tag_list)
