# Generated by Django 4.2.5 on 2023-11-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_rename_user_chatmessage_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user_id',
            new_name='user',
        ),
    ]
