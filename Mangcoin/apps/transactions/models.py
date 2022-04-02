from django.db import models
from apps.tokens.models import tokens

# PLATFORMS are multiple choices where user can choose someone
# The platforms are places where people can move their money
PLATFORMS = [
    ("WT", "Wallet"),
    ("EP", "Exchange point"),
    ("FT", "Fiat"),
    ("SW", "somewhere")
]

class transactions (models.Model):
    WALLET = "WT"
    EXCHANGE_POINT = "EP"
    FIAT = "FT"
    SOMWHERE = "SW"
    PLATFORMS = [
        (WALLET, "Wallet"),
        (EXCHANGE_POINT, "Exchange point"),
        (FIAT, "Fiat"),
        (SOMWHERE, "somewhere")
    ]

    transaction_id = models.BigAutoField(primary_key=True)
    transaction_date = models.DateField()
    origin = models.CharField(choices=PLATFORMS, default=SOMWHERE, max_length=255)
    destiny = models.CharField(choices=PLATFORMS, default=SOMWHERE, max_length=255)
    money_used = models.PositiveBigIntegerField(blank=True)
    token = models.ForeignKey(tokens, on_delete=models.CASCADE)
    token_aumont = models.FloatField()
    currently_token_price = models.FloatField()
    description = models.TextField()