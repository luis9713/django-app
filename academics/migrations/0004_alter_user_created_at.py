# Generated by Django 5.0.2 on 2024-03-11 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 11, 7, 7, 961599)),
        ),
    ]