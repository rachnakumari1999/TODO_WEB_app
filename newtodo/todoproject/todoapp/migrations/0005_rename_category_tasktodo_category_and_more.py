# Generated by Django 4.1.7 on 2023-05-30 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_rename_title_tasktodo_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasktodo',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='tasktodo',
            old_name='Description',
            new_name='description',
        ),
    ]
