# Generated by Django 4.2.7 on 2024-01-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0009_remove_technologycalculatorscore_technology_calculator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologycalculator',
            name='competitive',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='competitive_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='go_to_market',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='go_to_market_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='product_definition',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='product_definition_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='product_development',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='product_development_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='supply_chain',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='supply_chain_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='team',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='team_score',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='technology',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technologycalculator',
            name='technology_score',
            field=models.IntegerField(max_length=1),
        ),
    ]
