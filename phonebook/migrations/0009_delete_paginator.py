# Generated by Django 3.1.7 on 2021-03-02 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0008_paginator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paginator',
        ),
    ]