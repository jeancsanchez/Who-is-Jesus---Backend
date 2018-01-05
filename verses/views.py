from builtins import len, int
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import list_route
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

    @list_route(methods=['GET'])
    def filter(self, request):
        gospel_key = request.query_params.get('gospel_key')
        magic_number = int(request.query_params.get('magic_number'))

        queryset = Verse.objects.filter(gospel=gospel_key)
        len_queryset = len(queryset)
        index = int(magic_number/len_queryset)

        if index > len_queryset:
            index = int(index/len_queryset)

        serializer = VerseSerializer(queryset[index])
        return Response(serializer.data)
