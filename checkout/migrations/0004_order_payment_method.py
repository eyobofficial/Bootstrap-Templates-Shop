# Generated by Django 3.0.7 on 2021-01-31 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210131_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.IntegerField(blank=True, choices=[(1, 'PayPal'), (2, 'Stripe')], null=True),
        ),
    ]
