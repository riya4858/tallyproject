# Generated by Django 3.2.13 on 2022-06-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0020_group_nature_of_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='nature_of_group',
            field=models.CharField(max_length=225),
        ),
    ]
