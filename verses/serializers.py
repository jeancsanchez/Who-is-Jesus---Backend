from rest_framework import serializers

from verses.models import Verse


class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = '__all__'
