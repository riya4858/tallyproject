# Generated by Django 3.2.13 on 2022-06-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0002_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='books_begin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='fin_begin',
            field=models.DateField(null=True),
        ),
    ]