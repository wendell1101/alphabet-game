# Generated by Django 3.0.8 on 2020-07-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
