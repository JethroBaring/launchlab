# Generated by Django 4.2.7 on 2024-01-04 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readinesslevel', '0003_remove_scoringguide_level_criteria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoringguide',
            name='readiness_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_guides', to='readinesslevel.readinesslevel'),
        ),
    ]
