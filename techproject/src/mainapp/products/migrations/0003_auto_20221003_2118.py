# Generated by Django 2.1.5 on 2022-10-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221003_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]