# Generated by Django 3.1.6 on 2021-04-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20210409_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stipend',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]