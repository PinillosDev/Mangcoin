from django.db import models

class coins(models.Model):
    coin_id = models.BigAutoField(primary_key=True)
    coin_abbreviation = models.CharField(max_length=10)
    coin_name = models.CharField(max_length=255)
    fundation = models.DateField(blank=True)
    total_amount = models.PositiveBigIntegerField(blank=True)
    when_gets_one_dollar = models.DateField(blank=True)
    solution = models.CharField(max_length=100, blank=True)
    balance_equity = models.CharField(max_length=100, blank=True)
    is_stablecoin = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
