# Generated by Django 5.0.7 on 2024-07-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='api/songs/'),
        ),
    ]