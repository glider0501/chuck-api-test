REQUIRED_FIELDS = ['id', 'value', 'icon_url', 'url']

JOKE_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "value": {"type": "string", "minLength": 10},
        "icon_url": {"type": "string", "format": "uri"},
        "url": {"type": "string", "format": "uri"},
        "categories": {"type": "array", "items": {"type": "string"}}
    },
    "required": REQUIRED_FIELDS,
    "additionalProperties": True
}

SEARCH_RESPONSE_SCHEMA = {
    'type': 'object',
    'properties': {
        'result': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'icon_url': {'type': 'string'},
                    'id': {'type': 'string'},
                    'url': {'type': 'string'},
                    'value': {'type': 'string'},
                },
                'required': ['icon_url', 'id', 'url', 'value'],
            },
        },
        'total': {'type': 'integer'},
    },
    'required': ['result', 'total'],
}

CATEGORIES_RESPONSE_SCHEMA = {
    'type': 'array',
    'items': {'type': 'string'},
}
