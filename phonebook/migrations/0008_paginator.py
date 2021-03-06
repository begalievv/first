# Generated by Django 3.1.7 on 2021-03-02 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0007_auto_20210227_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paginator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)], verbose_name='Сколько должно быть справночников в одной странице?')),
            ],
        ),
    ]
