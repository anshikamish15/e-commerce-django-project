from django.db import models
from learn.models import UserProfile
from seller.models import Product



class Cart(models.Model):
	class Meta():
		unique_together = ('product', 'user')
		
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Orders(models.Model):
	order_id = models.CharField(max_length=100, unique=True)
	order_date = models.DateTimeField(auto_now=True)
	total_amt = models.DecimalField(decimal_places=3, max_digits=12)
	amt_status = models.CharField(max_length=20, default="unpaid")
	status = models.CharField(max_length=40, default="processing")
	placed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 


class OrderProduct(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.IntegerField()
	status = models.CharField(max_length=40, default="processing")