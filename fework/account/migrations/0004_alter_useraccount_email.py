# Generated by Django 4.2.5 on 2023-10-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_useraccount_otp_alter_useraccount_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
