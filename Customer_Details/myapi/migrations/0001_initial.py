# Generated by Django 3.0.1 on 2020-11-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bill', models.IntegerField(default=0)),
                ('mob_no', models.IntegerField()),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
    ]