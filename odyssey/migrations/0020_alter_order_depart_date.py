# Generated by Django 3.2.17 on 2023-04-03 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odyssey', '0019_auto_20230403_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='depart_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 15, 49, 0, 67178)),
        ),
    ]