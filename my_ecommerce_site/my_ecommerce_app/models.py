from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return f"{self.title}"

# * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *

class CartItem(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_cart_total = models.BooleanField(default=False)

    def update_total_price(self):
        self.total_price = self.product.price * self.quantity
        self.save()

    def __str__(self):
        if self.is_cart_total:
            return f"Cart total: {self.total_price}"
        else:
            return f"{self.title.title} x {self.quantity}"
# * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *

