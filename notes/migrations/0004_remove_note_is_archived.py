# Generated by Django 5.1.1 on 2024-10-06 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_is_archived_note_is_draft_note_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='is_archived',
        ),
    ]
