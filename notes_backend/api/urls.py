from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, NoteViewSet

router = DefaultRouter()
# The basename 'notes' will result in route paths /api/notes/ and /api/notes/{id}/
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('health/', health, name='Health'),
    path('', include(router.urls)),
]
