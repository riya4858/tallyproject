# Generated by Django 3.2.13 on 2022-08-22 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0009_auto_20220822_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='c_symbol',
            new_name='currency_symbol',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='end',
            new_name='fin_end',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='f_name',
            new_name='formal_name',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='states',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='active',
            new_name='status',
        ),
    ]
