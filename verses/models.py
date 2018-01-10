# -*- coding: utf-8  -*-
from __future__ import unicode_literals

from builtins import str
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

    verse = models.TextField(max_length=700, null=True)
    gospel = models.CharField(max_length=8, choices=GOSPELS)
    chapter_number = models.IntegerField(default=0, null=True)
    verse_begin = models.IntegerField(default=1, null=True)
    verse_end = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.gospel + " " + str(self.chapter_number) + " - " + str(self.verse_begin) + ", " + str(self.verse_end)

    class Meta:
        ordering = ('gospel', 'chapter_number', 'chapter_number', 'verse_begin', 'verse_end')
        verbose_name = 'Verso'
        verbose_name_plural = 'Versos'
