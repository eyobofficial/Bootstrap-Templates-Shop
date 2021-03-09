# Generated by Django 3.1.6 on 2021-03-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0006_category_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='repo_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='source_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='preview_url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
