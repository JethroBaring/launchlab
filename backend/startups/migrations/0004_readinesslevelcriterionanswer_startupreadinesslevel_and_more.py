# Generated by Django 4.2.7 on 2023-12-10 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("readinesslevel", "0001_initial"),
        ("startups", "0003_initialreadinesslevel_arl_response_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReadinessLevelCriterionAnswer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_deleted", models.DateTimeField(default=None, null=True)),
                ("score", models.SmallIntegerField()),
                ("remark", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "criterion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="readinesslevel.levelcriterion",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StartupReadinessLevel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_deleted", models.DateTimeField(default=None, null=True)),
                (
                    "readiness_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="startups_level",
                        to="readinesslevel.readinesslevel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="URATQuestionAnswer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_deleted", models.DateTimeField(default=None, null=True)),
                ("respone", models.CharField(max_length=500)),
                ("score", models.SmallIntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="readinesslevel",
            name="startup",
        ),
        migrations.RemoveField(
            model_name="startup",
            name="is_qualified",
        ),
        migrations.AddField(
            model_name="startup",
            name="qualification_status",
            field=models.IntegerField(
                choices=[(1, "Pending"), (2, "Rated"), (3, "Qualified")], default=1
            ),
        ),
        migrations.DeleteModel(
            name="InitialReadinessLevel",
        ),
        migrations.DeleteModel(
            name="ReadinessLevel",
        ),
        migrations.AddField(
            model_name="uratquestionanswer",
            name="startup",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urat_question_answers",
                to="startups.startup",
            ),
        ),
        migrations.AddField(
            model_name="uratquestionanswer",
            name="urat_question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="readinesslevel.uratquestion",
            ),
        ),
        migrations.AddField(
            model_name="startupreadinesslevel",
            name="startup",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="readiness_levels",
                to="startups.startup",
            ),
        ),
        migrations.AddField(
            model_name="readinesslevelcriterionanswer",
            name="startup",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="readiness_evel_criterion_answers",
                to="startups.startup",
            ),
        ),
    ]