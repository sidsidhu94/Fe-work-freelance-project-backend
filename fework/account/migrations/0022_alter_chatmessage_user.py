# Generated by Django 4.2.5 on 2023-11-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_rename_user_id_chatmessage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.useraccount'),
        ),
    ]