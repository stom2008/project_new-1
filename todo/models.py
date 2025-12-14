from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Product(models.Model):
    # one to many
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank = True, null=True)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product2(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    
class Product3w(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    