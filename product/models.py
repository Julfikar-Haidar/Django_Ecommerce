from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('Pending', 'PENDING'),
        ('Published', 'PUBLISHED'),
        ('Stock Out', 'STOCK OUT')
    )

    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_image', null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Create your models here.
