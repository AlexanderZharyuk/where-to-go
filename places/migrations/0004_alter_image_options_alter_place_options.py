# Generated by Django 4.1 on 2022-08-29 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-position']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'место', 'verbose_name_plural': 'Места'},
        ),
    ]
