# Generated by Django 4.0.5 on 2022-06-27 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='new_field',
        ),
    ]
