from rest_framework import serializers


# Custom validators for many-to-many through serializer of Specification
def is_dict(data, name):
    if isinstance(data, dict):
        return True
    else:
        raise serializers.ValidationError(f"{name} must be a valid dict.")

def is_list(data, name):
    if isinstance(data, list):
        return True
    else:
        raise serializers.ValidationError(f"{name} must be a valid list.")
