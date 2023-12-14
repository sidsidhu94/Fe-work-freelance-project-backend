# Generated by Django 4.2.5 on 2023-12-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_workappreciation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_months', models.PositiveIntegerField(choices=[(6, '6 months'), (12, '1 year'), (24, '2 years')])),
            ],
        ),
    ]
