# Generated by Django 4.2.5 on 2023-12-14 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_payment_premium_selected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='user_id',
        ),
    ]