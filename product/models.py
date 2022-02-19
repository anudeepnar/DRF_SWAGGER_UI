from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='products' ,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
