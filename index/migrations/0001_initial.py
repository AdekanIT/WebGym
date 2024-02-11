# Generated by Django 5.0.1 on 2024-02-11 04:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('data_crate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BranchInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('data_crate', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.branches')),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField(blank=True)),
                ('experience', models.IntegerField(blank=True)),
                ('character', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='static/media/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=16)),
                ('price', models.FloatField(blank=True)),
                ('data_add', models.DateTimeField(auto_now_add=True)),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.branches')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.TextField()),
                ('user_data', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.instructors')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('subscription', models.IntegerField(blank=True)),
                ('phone_num', models.CharField(max_length=256)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('sub_inst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.instructors')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
