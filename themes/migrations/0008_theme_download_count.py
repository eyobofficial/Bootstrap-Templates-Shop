# Generated by Django 3.0.7 on 2020-09-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0007_theme_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
