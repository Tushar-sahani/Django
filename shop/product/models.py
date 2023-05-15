from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    

class Address(models.Model):
    street = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.country}"
    

class Brand(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=10)
    image = models.ImageField(blank=True,upload_to='product_img')
    brand = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.slug = self.id
        super().save(*args,**kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=15)
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.product} - Raiting {self.rating}"


