# Generated by Django 3.2.13 on 2022-08-11 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('mailing_name', models.CharField(max_length=225)),
                ('address1', models.CharField(max_length=225)),
                ('address2', models.CharField(max_length=225)),
                ('address3', models.CharField(max_length=225)),
                ('address4', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=6)),
                ('telephone', models.CharField(max_length=225)),
                ('mobile', models.CharField(max_length=225)),
                ('fax', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=225)),
                ('fin_begin', models.DateField(null=True)),
                ('books_begin', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('end', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('currency_symbol', models.CharField(blank=True, max_length=225)),
                ('formal_name', models.CharField(blank=True, max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('provide_banking_details', models.CharField(max_length=225)),
                ('pan_no', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('voucher_type', models.CharField(max_length=225)),
                ('abbreviation', models.CharField(max_length=225)),
                ('active_this_voucher_type', models.CharField(max_length=225)),
                ('method_voucher_numbering', models.CharField(max_length=225)),
                ('use_adv_conf', models.CharField(blank=True, max_length=225)),
                ('prvnt_duplictes', models.CharField(blank=True, default='Null', max_length=225)),
                ('use_effective_date', models.CharField(default='Null', max_length=225)),
                ('allow_zero_value_trns', models.CharField(max_length=225)),
                ('allow_naration_in_voucher', models.CharField(max_length=225)),
                ('make_optional', models.CharField(max_length=225)),
                ('provide_naration', models.CharField(max_length=225)),
                ('print_voucher', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(blank=True, max_length=225)),
                ('region_name', models.CharField(blank=True, max_length=225)),
                ('division_name', models.CharField(blank=True, max_length=225)),
                ('district_name', models.CharField(blank=True, max_length=225)),
                ('province_name', models.CharField(blank=True, max_length=225)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Sundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_balance_bill_by_bill', models.CharField(blank=True, default='Null', max_length=225)),
                ('default_credit_period', models.CharField(blank=True, default='Null', max_length=225)),
                ('check_for_credit_days', models.CharField(blank=True, default='Null', max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Mailing_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailingname', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('country', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Banking_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_limit', models.CharField(max_length=225)),
                ('holder_name', models.CharField(max_length=225)),
                ('acc_no', models.CharField(max_length=225)),
                ('ifsc', models.CharField(max_length=225)),
                ('swift_code', models.CharField(max_length=225)),
                ('bank_name', models.CharField(max_length=225)),
                ('branch', models.CharField(max_length=225)),
                ('set_cheque', models.CharField(max_length=225)),
                ('ch_printing', models.CharField(max_length=225)),
                ('ch_config', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Asset_Statutory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessable_calculation', models.CharField(max_length=225)),
                ('appropriate_to', models.CharField(max_length=225)),
                ('gst_applicable', models.CharField(max_length=225)),
                ('set_alter_GST', models.CharField(max_length=225)),
                ('type_of_supply', models.CharField(max_length=225)),
                ('method_of_calc', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Asset_Rounding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounding_method', models.CharField(max_length=225)),
                ('round_limit', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Gst_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=225)),
                ('reg_type', models.CharField(max_length=225)),
                ('assessee', models.CharField(max_length=225)),
                ('app_form', models.CharField(max_length=225)),
                ('gstin', models.CharField(max_length=225)),
                ('gstr1', models.CharField(max_length=225)),
                ('flood', models.CharField(max_length=225)),
                ('rate_details', models.CharField(max_length=225)),
                ('advance_receipts', models.CharField(max_length=225)),
                ('reverse_charge', models.CharField(max_length=225)),
                ('classifications', models.CharField(max_length=225)),
                ('bend_details', models.CharField(max_length=225)),
                ('eway_bill', models.CharField(max_length=225)),
                ('applicable_form', models.CharField(max_length=225)),
                ('threshold_includes', models.CharField(max_length=225)),
                ('threshold_limit', models.CharField(max_length=225)),
                ('intrastate', models.CharField(max_length=225)),
                ('threshold_limit1', models.CharField(max_length=225)),
                ('print_eway', models.CharField(max_length=225)),
                ('e_invoice', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225, null=True)),
                ('under', models.CharField(max_length=225)),
                ('sub_ledger', models.BooleanField(default=False)),
                ('debit_credit', models.BooleanField(default=False)),
                ('calculation', models.BooleanField(default=False)),
                ('used_purchase', models.CharField(blank=True, max_length=225, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_accounts', models.BooleanField(default=True)),
                ('bill_wise_entry', models.BooleanField(default=True)),
                ('cost_centres', models.BooleanField(default=False)),
                ('interest_calc', models.BooleanField(default=True)),
                ('maintain_inventory', models.BooleanField(default=True)),
                ('integrate_accounts', models.BooleanField(default=True)),
                ('multiple_price_level', models.BooleanField(default=True)),
                ('batches', models.BooleanField(default=True)),
                ('expirydate_batches', models.BooleanField(default=True)),
                ('joborder_processing', models.BooleanField(default=True)),
                ('sub_ledger', models.BooleanField(default=True)),
                ('cost_tracking', models.BooleanField(default=True)),
                ('job_costing', models.BooleanField(default=True)),
                ('discount_invoices', models.BooleanField(default=True)),
                ('Billed_Quantity', models.BooleanField(default=True)),
                ('gst', models.BooleanField(default=False)),
                ('tds', models.BooleanField(default=False)),
                ('tcs', models.BooleanField(default=False)),
                ('vat', models.BooleanField(default=False)),
                ('excise', models.BooleanField(default=True)),
                ('servicetax', models.BooleanField(default=True)),
                ('payroll', models.BooleanField(default=False)),
                ('multiple_addrss', models.BooleanField(default=True)),
                ('vouchers', models.BooleanField(default=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('currency_code', models.CharField(max_length=225)),
                ('decimal_places', models.CharField(max_length=225)),
                ('show_in_millions', models.BooleanField(default=False)),
                ('suffix_symbol', models.BooleanField(default=False)),
                ('symbol_and_amount', models.BooleanField(default=False)),
                ('after_decimal', models.CharField(max_length=225)),
                ('amount_in_words', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Costcentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225, null=True)),
                ('under', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('mailing_name', models.CharField(max_length=225)),
                ('address1', models.CharField(max_length=225)),
                ('address2', models.CharField(max_length=225)),
                ('address3', models.CharField(max_length=225)),
                ('address4', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=6)),
                ('telephone', models.CharField(max_length=225)),
                ('mobile', models.CharField(max_length=225)),
                ('fax', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=225)),
                ('fin_begin', models.DateField(null=True)),
                ('books_begin', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('end', models.DateField(null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.countries')),
                ('states', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.states')),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.countries'),
        ),
        migrations.AddField(
            model_name='companies',
            name='states',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.states'),
        ),
    ]
