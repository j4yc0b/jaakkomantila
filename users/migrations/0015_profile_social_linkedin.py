# Generated by Django 4.0.5 on 2022-07-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
