from requests import post, put

from utils import EventContent


def add_actions():
    return {
        "webhook": {
            "operation": webhook,
            "name": "Webhook",
            "data_fields": [
                {
                    "key": "url",
                    "label": "URL",
                    "field_type": "text",
                    "field_options": {
                        "format": "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]"
                                  "{1,256}\.[a-zA-Z0-9()]{1,6}"
                                  "\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
                        "data_type": "string"
                    }
                }, {
                    "key": "method",
                    "field_type": "select",
                    "field_options": {
                        "default": "POST",
                        "options": [
                            {
                                "label": "POST",
                                "value": "post"
                            },
                            {
                                "label": "PUT",
                                "value": "put"
                            }
                        ]
                    }
                }, {
                    "key": "payload",
                    "field_type": "text",
                    "field_options": {
                        "limit": 5000,
                        "hint": "Conteúdo do hook",
                        "data_type": "string"
                    }
                }, {
                    "key": "headers",
                    "label": "Headers",
                    "field_type": "object",
                    "field_options": {
                        "limit": 50,
                        "property_key": {
                            "label": "Header",
                            "field_type": "text",
                            "field_options": {}
                        },
                        "property_value": {
                            "label": "Conteúdo",
                            "field_type": "text",
                            "field_options": {}
                        }
                    }
                }
            ]
        }
    }


methods = {"POST": post, "PUT": put}


def webhook(event_content: EventContent, data):
    webhook_method = data.get('method')
    webhook_url = data.get('url')
    webhook_headers = data.get('headers')
    webhook_payload = data.get('payload')

    for _ in range(3):
        r = methods.get(webhook_method, post)(url=webhook_url,
                                              data=webhook_payload,
                                              headers=webhook_headers)
        if r.ok:
            break
