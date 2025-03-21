# Generated by Django 5.1.6 on 2025-03-10 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=75)),
                ('data_file', models.FileField(upload_to='uploads/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.department')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.region')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
