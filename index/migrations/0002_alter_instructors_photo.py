# Generated by Django 5.0.1 on 2024-02-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructors',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]