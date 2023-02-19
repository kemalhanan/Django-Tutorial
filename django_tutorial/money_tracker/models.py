from django.db import models

# Create your models here.
class TransactionRecord(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
