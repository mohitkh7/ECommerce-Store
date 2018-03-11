from django.db import models
from django.utils.crypto import get_random_string 

# Create your models here.
class Order(models.Model):
	token = models.CharField(max_length=6,unique=True,null=True)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)
	email = models.EmailField(null=True)
	contact_no = models.PositiveIntegerField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	def save(self,*args,**kwargs):
		if self.pk is None:
			self.token = get_random_string(length=6)
		super(Order, self).save(*args, **kwargs)

	def total_price(self):
		price = 0
		for item in self.orderitem_set.all():
			price += item.quantity*item.price
		return price

	def total_item(self):
		return self.orderitem_set.count()

	def total_quantity(self):
		quantity = 0
		for item in self.orderitem_set.all():
			quantity += item.quantity
		return quantity

class OrderItem(models.Model):
	order = models.ForeignKey('Order')
	product = models.ForeignKey('web.Product')
	quantity = models.PositiveIntegerField(default=1)
	price = models.PositiveIntegerField()
