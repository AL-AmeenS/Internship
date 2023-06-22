from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products', null=True, default=None)
    registration_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def is_active(self):
        current_date = timezone.now()
        registered_before = current_date - self.registration_date
        return registered_before.days >= 60
