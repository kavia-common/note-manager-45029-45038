from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note model with basic validation."""

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """Ensure title is provided and not empty."""
        if value is None or str(value).strip() == "":
            raise serializers.ValidationError("Title is required.")
        return value
