# Generated by Django 4.2.16 on 2024-10-09 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_galary_file_type_alter_about_thumbnail_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Galary',
            new_name='Gallery',
        ),
    ]
