# Generated by Django 3.2.17 on 2023-03-27 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odyssey', '0012_alter_loginping_pingtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='departDate',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ticketCount',
        ),
    ]
