# Generated by Django 3.1.7 on 2021-02-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.IntegerField(default=312)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
            ],
        ),
    ]
