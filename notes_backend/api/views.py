from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """Simple health check endpoint."""
    return Response({"message": "Server is up!"})


class NoteViewSet(viewsets.ModelViewSet):
    """
    PUBLIC_INTERFACE
    A ViewSet that provides the standard CRUD actions for Notes.

    Endpoints:
    - GET /api/notes/ -> list notes (paginated)
    - POST /api/notes/ -> create a new note
    - GET /api/notes/{id}/ -> retrieve note
    - PUT /api/notes/{id}/ -> update note (full)
    - PATCH /api/notes/{id}/ -> partial update note
    - DELETE /api/notes/{id}/ -> delete note
    """
    queryset = Note.objects.all().order_by("-updated_at", "-id")
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]
