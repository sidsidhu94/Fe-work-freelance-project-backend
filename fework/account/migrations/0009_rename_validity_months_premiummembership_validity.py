# Generated by Django 4.2.5 on 2023-12-04 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userprofile_premium'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premiummembership',
            old_name='validity_months',
            new_name='Validity',
        ),
    ]
