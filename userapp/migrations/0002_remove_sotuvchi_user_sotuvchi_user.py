# Generated by Django 4.1.3 on 2023-01-09 11:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotuvchi',
            name='user',
        ),
        migrations.AddField(
            model_name='sotuvchi',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
