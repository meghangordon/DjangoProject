# Generated by Django 4.1.2 on 2022-10-21 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TransactionTypes',
            new_name='Transaction',
        ),
    ]
