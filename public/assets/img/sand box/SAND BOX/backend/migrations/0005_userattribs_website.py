# Generated by Django 3.1.7 on 2021-04-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210330_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='userattribs',
            name='website',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]