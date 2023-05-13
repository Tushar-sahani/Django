from django.db import models

class Profile(models.Model):
    user_email = models.EmailField()
    full_name = models.CharField(max_length=20)
    DOB = models.DateField()
    brand = models.CharField(max_length=30,null=True)
# Create your models here.
