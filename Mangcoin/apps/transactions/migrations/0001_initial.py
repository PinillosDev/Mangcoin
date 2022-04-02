# Generated by Django 4.0.3 on 2022-04-02 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField(default='%m/%d/%Y')),
                ('origin', models.CharField(choices=[('WT', 'Wallet'), ('EP', 'Exchange point'), ('FT', 'Fiat'), ('SW', 'somwhere')], default='SW', max_length=255)),
                ('destiny', models.CharField(choices=[('WT', 'Wallet'), ('EP', 'Exchange point'), ('FT', 'Fiat'), ('SW', 'somwhere')], default='SW', max_length=255)),
                ('money_used', models.PositiveBigIntegerField(blank=True)),
                ('token_aumont', models.PositiveIntegerField()),
                ('currently_token_price', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.tokens')),
            ],
        ),
    ]
