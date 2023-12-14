# Generated by Django 4.2.5 on 2023-12-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_payment_premium_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(max_length=255, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=255, verbose_name='Payment ID'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='signature',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Signature'),
        ),
    ]
