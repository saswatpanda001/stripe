# Generated by Django 4.2.2 on 2023-08-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_price_plans_price_m_plans_price_y'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='price_y',
        ),
    ]
