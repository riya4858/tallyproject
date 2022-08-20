# Generated by Django 3.2.13 on 2022-08-19 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0003_auto_20220811_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='rateofexchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdrate', models.CharField(max_length=225)),
                ('sell_voucher_rate', models.CharField(max_length=225)),
                ('sell_specified_rate', models.CharField(max_length=225)),
                ('buy_voucher_rate', models.CharField(max_length=225)),
                ('buy_specified_rate', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.currency')),
            ],
        ),
    ]
