from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title