# Generated by Django 4.2.5 on 2023-11-27 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['timestamp'], 'verbose_name_plural': 'Message'},
        ),
        migrations.DeleteModel(
            name='WorkAppreciation',
        ),
    ]