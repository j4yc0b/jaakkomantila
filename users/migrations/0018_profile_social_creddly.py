# Generated by Django 4.0.5 on 2022-07-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_social_upwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_creddly',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
