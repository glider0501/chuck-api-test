from jsonschema import validate, ValidationError


class SchemaValidator:
    """Validates JSON responses against schemas."""

    @staticmethod
    def validate(data, schema):
        """Validate data against schema."""
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed: {e.message}")

    @staticmethod
    def validate_joke(joke):
        """Validate joke response structure."""
        required_fields = ['icon_url', 'id', 'url', 'value']
        for field in required_fields:
            if field not in joke:
                raise AssertionError(f"Missing required field: {field}")
            if not isinstance(joke[field], str):
                raise AssertionError(f"Field {field} should be string")
