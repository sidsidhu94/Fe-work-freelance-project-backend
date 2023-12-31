# Generated by Django 4.2.5 on 2023-11-30 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_userconnection_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkAppreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0, null=True)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userwork')),
            ],
        ),
    ]
