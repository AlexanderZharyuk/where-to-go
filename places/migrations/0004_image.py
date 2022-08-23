# Generated by Django 4.1 on 2022-08-23 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/', verbose_name='Картинки места')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место')),
            ],
        ),
    ]