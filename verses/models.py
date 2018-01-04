from __future__ import unicode_literals

from django.db import models


class Verse(models.Model):
    verse = models.CharField(max_length=300, null=True)
    chapter_number = models.IntegerField(default=0, null=True)
    verse_begin = models.IntegerField(default=1, null=True)
    verse_end = models.IntegerField(default=1, null=True)

