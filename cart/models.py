
from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.

class CartItem(models.Model):
    """Item in a user's persistent cart."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"