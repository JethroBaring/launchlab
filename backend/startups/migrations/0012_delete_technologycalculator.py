# Generated by Django 4.2.7 on 2024-01-05 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0011_rename_startup_id_technologycalculator_startup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TechnologyCalculator',
        ),
    ]