from django.contrib.auth.models import User
from django.db import models

from Product.models import Product


class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    total_price=models.IntegerField(blank=True,null=True)
    date_paid=models.DateField()

    def __str__(self):
        return self.user.username

class order_detail(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    price=models.IntegerField()
    count=models.IntegerField()
    color=models.CharField(max_length=50,null=True,blank=True)
