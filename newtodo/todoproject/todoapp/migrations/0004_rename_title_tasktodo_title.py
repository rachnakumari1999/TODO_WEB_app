# Generated by Django 4.1.7 on 2023-05-30 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_dete_tasktodo_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasktodo',
            old_name='Title',
            new_name='title',
        ),
    ]
