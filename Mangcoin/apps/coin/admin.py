from django.contrib import admin
from apps.coin.models import coins

admin.site.register(coins) # It enables manage the database from Django's admin
