# Generated by Django 3.1.7 on 2021-04-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_project_question_project_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_question',
            name='project_id',
        ),
        migrations.AddField(
            model_name='project_question',
            name='rel_project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.project'),
        ),
    ]
