# Generated by Django 4.2.2 on 2023-08-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_plans_usersubscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='price',
            new_name='price_m',
        ),
        migrations.AddField(
            model_name='plans',
            name='price_y',
            field=models.FloatField(blank=True, null=True),
        ),
    ]