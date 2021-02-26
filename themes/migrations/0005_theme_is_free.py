# Generated by Django 3.1.6 on 2021-02-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0004_auto_20210220_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='is_free',
            field=models.BooleanField(default=False, help_text='Not a premium theme.', verbose_name='free'),
        ),
    ]
