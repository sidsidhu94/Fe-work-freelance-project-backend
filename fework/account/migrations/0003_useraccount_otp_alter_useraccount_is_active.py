# Generated by Django 4.2.5 on 2023-10-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_useraccount_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]