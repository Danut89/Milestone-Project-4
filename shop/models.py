from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('equipment', 'Equipment'),
        ('clothing', 'Clothing'),
        ('supplement', 'Supplement'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    sku = models.CharField(max_length=20, blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

