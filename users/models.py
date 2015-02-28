from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user_name