# Generated by Django 4.1 on 2022-08-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_image_is_main_image_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='images',
            new_name='image',
        ),
    ]