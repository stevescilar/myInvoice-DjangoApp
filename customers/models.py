from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

