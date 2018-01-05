from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from verses.models import Verse
from verses.serializers import VerseSerializer


class VerseViewSet(ViewSet):
    """
       A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = Verse.objects.all()
        serializer = VerseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Verse.objects.all()
        verse = get_object_or_404(queryset, pk=pk)
        serializer = VerseSerializer(verse)
        return Response(serializer.data)
