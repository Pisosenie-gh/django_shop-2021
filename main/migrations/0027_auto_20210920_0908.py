# Generated by Django 3.2.7 on 2021-09-20 09:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0026_contests_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contests',
            name='likes',
        ),
        migrations.AddField(
            model_name='contests',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]