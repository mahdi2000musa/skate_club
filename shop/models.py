from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    image = models.ImageField(upload_to="product/")
    price = models.IntegerField(blank=False, null=False)
    num_of_buy = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.title


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_cart_total_price(self):
        items = self.cartitem_set.all()
        total = sum([item.get_total() for item in items])
        return total

    def get_cart_total_items(self):
        items = self.cartitem_set.all()
        total = sum([item.quantity for item in items])
        return total



class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title

    def get_total(self):
        total = self.product.price * self.quantity
        return total




