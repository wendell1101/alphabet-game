# Generated by Django 3.0.8 on 2020-07-01 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_image_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game',
            new_name='GameImage',
        ),
        migrations.RenameField(
            model_name='gameimage',
            old_name='image_name',
            new_name='name',
        ),
    ]