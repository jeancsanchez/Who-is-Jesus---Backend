from __future__ import unicode_literals

from django.db import models


# noinspection SpellCheckingInspection
class Verse(models.Model):
    GOSPELS = (
        ('Mt', 'Mateus'),
        ('Lc', 'Lucas'),
        ('Mc', 'Marcos'),
        ('Jo', 'João'),
        ('At', 'Atos dos apóstolos'),
        ('Rom', 'Romanos'),
        ('I Cor', 'Primeira epístola Coríntios'),
        ('II Cor', 'Segunda epístolas Coríntios'),
        ('Gal', 'Gálatas'),
        ('Ef', 'Efésios'),
        ('Flp', 'Filipenses'),
        ('Col', 'Colossenses'),
        ('I Tes', 'Primeira epístola Tessalonicenses'),
        ('II Tes', 'Segunda epístola Tessalonicenses'),
        ('I Tim', 'Primeira epístola a Timóteo'),
        ('II Tim', 'Primeira epístola a Timóteo')
    )

    verse = models.TextField(max_length=300, null=True)
    gospel = models.CharField(max_length=8, choices=GOSPELS)
    chapter_number = models.IntegerField(default=0, null=True)
    verse_begin = models.IntegerField(default=1, null=True)
    verse_end = models.IntegerField(default=1, null=True)
