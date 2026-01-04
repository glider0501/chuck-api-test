def assert_joke_structure(joke):
    """Assert that joke has proper structure."""
    required_fields = ['icon_url', 'id', 'url', 'value']

    for field in required_fields:
        assert field in joke, f"Missing field: {field}"
        assert isinstance(joke[field], str), f"Field {field} should be string"

    assert len(joke['id']) > 0, "ID cannot be empty"
    assert len(joke['value']) > 0, "Value cannot be empty"
    assert 'http' in joke['icon_url'].lower(), "Invalid icon URL"