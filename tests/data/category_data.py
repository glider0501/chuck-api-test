from random import sample
import uuid

KNOWN_CATEGORIES = [
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

CATEGORY_COUNT = len(KNOWN_CATEGORIES)
INVALID_CATEGORY = uuid.uuid4().hex[:12]
SAMPLE_CATEGORIES = sample(KNOWN_CATEGORIES, 5)
