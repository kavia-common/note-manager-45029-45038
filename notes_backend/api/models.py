from django.db import models


class Note(models.Model):
    """
    A simple Note model to store user notes.

    Fields:
    - title: Required short title of the note.
    - content: Optional longer content body.
    - created_at: Auto timestamp when the note is created.
    - updated_at: Auto timestamp when the note is updated.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"
