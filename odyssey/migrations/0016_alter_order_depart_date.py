# Generated by Django 3.2.17 on 2023-03-31 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odyssey', '0015_auto_20230331_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='depart_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 3, 2, 38, 52, 53503)),
        ),
    ]