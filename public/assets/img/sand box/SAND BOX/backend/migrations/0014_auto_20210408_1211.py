# Generated by Django 3.1.7 on 2021-04-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20210407_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userattribs',
            name='applied_projects',
        ),
        migrations.AddField(
            model_name='project',
            name='applied_users',
            field=models.ManyToManyField(blank=True, null=True, to='backend.UserAttribs'),
        ),
    ]
