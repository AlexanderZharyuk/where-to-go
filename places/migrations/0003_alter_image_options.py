# Generated by Django 4.1 on 2022-08-24 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
    ]