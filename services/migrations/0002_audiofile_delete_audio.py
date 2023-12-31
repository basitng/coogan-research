# Generated by Django 4.2.2 on 2023-06-14 11:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', cloudinary.models.CloudinaryField(max_length=255)),
                ('transcript', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
