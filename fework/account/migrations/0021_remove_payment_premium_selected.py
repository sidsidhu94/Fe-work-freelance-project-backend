# Generated by Django 4.2.5 on 2023-12-14 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_payment_order_id_alter_payment_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='premium_selected',
        ),
    ]
