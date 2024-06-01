# Generated by Django 5.0.3 on 2024-04-16 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordgradebyscience',
            name='average_grade_number',
            field=models.FloatField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='wordgradebyscience',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 16, 19, 10, 13, 598818), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='wordgradebyscience',
            name='modification_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 16, 19, 10, 13, 598818), verbose_name='date modified'),
        ),
        migrations.AlterField(
            model_name='wordgradebyscience',
            name='token_grade_list',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]