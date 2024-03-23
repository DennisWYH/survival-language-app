# Generated by Django 4.2.11 on 2024-03-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_alter_card_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='grade',
            field=models.CharField(choices=[('8', 'rainbow'), ('7a+', 'mint'), ('7a', 'White'), ('6c+', 'purple'), ('6c', 'red'), ('6b+', 'DarkBlue'), ('6b', 'Yellow'), ('6a+', 'Orange'), ('6a', 'Black'), ('5', 'LightBlue'), ('4', 'Green')], default='', max_length=3, verbose_name='grade'),
        ),
    ]