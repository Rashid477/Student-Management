# Generated by Django 5.0.2 on 2024-03-01 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='TeacherName')),
                ('Age', models.PositiveIntegerField()),
                ('Department', models.CharField(max_length=50)),
                ('Experience', models.TextField(blank=True)),
                ('Phoneno', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Teach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]