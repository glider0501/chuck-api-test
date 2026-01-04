JOKE_RESPONSE_SCHEMA = {
    'type': 'object',
    'properties': {
        'icon_url': {'type': 'string'},
        'id': {'type': 'string'},
        'url': {'type': 'string'},
        'value': {'type': 'string'},
    },
    'required': ['icon_url', 'id', 'url', 'value'],
    'additionalProperties': False,
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