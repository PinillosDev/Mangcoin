from django.db import models
from ...Mangcoin import settings
from ..tokens.models import tokens

PLATFORMS = (
    ("Wallet"),
    ("Exchange point"),
    ("DeFi"),
    ("somwhere")
)

class transactions(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    transaction_date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    origin = models.CharField(choices=PLATFORMS, default="somwhere")
    destiny = models.CharField(choices=PLATFORMS, default="somwhere")
    money_used = models.PositiveBigIntegerField(blank=True)
    token = models.ForeignKey(tokens, on_delete=models.CASCADE)
    token_aumont = models.PositiveIntegerField()
    currently_token_price = models.PositiveSmallIntegerField()
    description = models.TextField()