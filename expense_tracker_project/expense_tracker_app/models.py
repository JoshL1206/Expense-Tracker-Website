from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"