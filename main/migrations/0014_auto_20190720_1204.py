# Generated by Django 2.2.2 on 2019-07-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_meeting_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='anonym.png', upload_to=''),
        ),
    ]
