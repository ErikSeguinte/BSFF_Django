# Generated by Django 3.1.11 on 2021-05-17 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['full_name']},
        ),
    ]
