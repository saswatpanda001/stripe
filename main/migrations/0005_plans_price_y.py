# Generated by Django 4.2.2 on 2023-08-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_plans_price_y'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='price_y',
            field=models.FloatField(blank=True, null=True),
        ),
    ]