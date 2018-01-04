# Generated by Django 2.0.1 on 2018-01-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.CharField(max_length=300, null=True)),
                ('chapter_number', models.IntegerField(default=0, null=True)),
                ('verse_begin', models.IntegerField(default=1, null=True)),
                ('verse_end', models.IntegerField(default=1, null=True)),
            ],
        ),
    ]