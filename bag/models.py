from django.db import models
from django.utils import timezone

# Create your models here.
class Bag(models.Model):
	product= models.ForeignKey('web.Product')
	customer_id = models.CharField(max_length=200)#can be user id or unique_session_id
	quantity = models.PositiveSmallIntegerField(default=1)
	price = models.PositiveSmallIntegerField(null=True)
	is_removed = models.BooleanField(default=False)
	is_ordered = models.BooleanField(default=False)
	added_on = models.DateTimeField(auto_now_add = True)
	modified_on  =  models.DateTimeField(auto_now = True)


	def total_price(self):
		return self.quantity * int(self.price)