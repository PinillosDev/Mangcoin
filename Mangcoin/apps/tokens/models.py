from django.db import models

class tokens(models.Model):
    token_id = models.CharField(max_length=10, primary_key=True)
    token_name = models.CharField(max_length=255)
    fundation_year = models.PositiveSmallIntegerField(blank=True)
    total_aumont = models.PositiveSmallIntegerField(blank=True)