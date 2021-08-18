from utils import EventContent


def add_actions():
    return {
        "add_timelines": {
            "operation": add_timelines,
            "name": "Adicionar à timeline",
            "data_fields": [
                {
                    "field_type": "array",
                    "key": "timelines",
                    "label": "Timelines",
                    "field_options": {
                        "label": "Timeline",
                        "field_type": "select",
                        "field_options": {
                            "from": {
                                "url": "https://smartview-api.novaweb.duckdns.org:16443/v1/timeline/",
                                "optionsPath": "data.results",
                                "label": "name",
                                "value": "id_"
                            }
                        }
                    }
                }
            ]
        }
    }


def add_timelines(event_content: EventContent, data):
    timelines: list = data.get('timelines')
    event_content['event']['content']['timelines'].extend(timelines)
    event_content['event']['content']['timelines'] \
        = list(set(event_content['event']['content']['timelines']))

    return event_content
