from rest_framework.viewsets import ModelViewSet
from notes_app.models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer