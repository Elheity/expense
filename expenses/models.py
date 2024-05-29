from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_expense = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.type_of_expense} - {self.amount}"
