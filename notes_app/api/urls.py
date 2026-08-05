from django.urls import path, include
from .views import NoteViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]