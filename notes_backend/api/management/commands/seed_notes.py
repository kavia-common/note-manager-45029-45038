from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Seed the database with sample notes."

    def handle(self, *args, **options):
        examples = [
            {"title": "Welcome", "content": "This is your first note."},
            {"title": "Todo", "content": "1) Add more notes\n2) Build a UI"},
            {"title": "Ideas", "content": "Use tags, search, and sharing."},
        ]
        created_count = 0
        for ex in examples:
            obj, created = Note.objects.get_or_create(title=ex["title"], defaults={"content": ex["content"]})
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created_count} new notes."))
