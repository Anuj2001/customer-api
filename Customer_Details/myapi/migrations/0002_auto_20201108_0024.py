# Generated by Django 3.0.1 on 2020-11-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mob_no',
            field=models.CharField(max_length=13),
        ),
    ]
