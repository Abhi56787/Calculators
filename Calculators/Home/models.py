from Home.views import monthly_investment
from django.db import models

# Create your models here.
class MonthlyInv(models.Model):
    monthly_investment = models.CharField(max_length=30)
    years = models.CharField(max_length=30)
    exp_ret = models.CharField(max_length=30)

