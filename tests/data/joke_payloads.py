
JOKE_CATEGORIES = [
    'animal',
    'career',
    'celebrity',
    'dev',
    'explicit',
    'fashion',
    'food',
    'history',
    'money',
    'movie',
    'music',
    'political',
    'religion',
    'science',
    'sport',
    'travel',
]

SEARCH_TEST_CASES = [
    {
        'id': 'search-chuck',
        'query': 'chuck',
        'min_results': 1,
    },
    {
        'id': 'search-norris',
        'query': 'norris',
        'min_results': 1,
    },
    {
        'id': 'search-kicks',
        'query': 'kicks',
        'min_results': 0,
    },
    {
        'id': 'search-funny',
        'query': 'funny',
        'min_results': 0,
    },
    {
        'id': 'search-world',
        'query': 'world',
        'min_results': 0,
    },
    {
        'id': 'search-action',
        'query': 'action',
        'min_results': 0,
    },
    {
        'id': 'search-java',
        'query': 'java',
        'min_results': 0,
    },
    {
        'id': 'search-programming',
        'query': 'programming',
        'min_results': 0,
    },
]

INVALID_SEARCH_INPUTS = [
    {
        'description': 'empty-string',
        'query': '',
    },
    {
        'description': 'only-spaces',
        'query': '   ',
    },
    {
        'description': 'sql-injection',
        'query': "'; DROP TABLE jokes; --",
    },
    {
        'description': 'xss-attempt',
        'query': '<script>alert("xss")</script>',
    },
]