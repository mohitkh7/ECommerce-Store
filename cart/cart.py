from decimal import Decimal
from django.conf import settings
from web.models import Product
class Cart(object):

	def __init__(self,request):
		"""
		Initialize the cart
		"""
		self.session = request.session
		cart = self.session.get('cart')
		if not cart:
			# save an empty cart in the session
			cart = self.session['cart'] = {}
		self.cart = cart

	def add(self,product,quantity=1,update_quantity=False):
		"""
		Add a product or update its quantity
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0,'price':str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		#update cart
		self.session['cart'] = self.cart
		#mark session as modified
		self.session.modified = True

	def remove(self,product):
		"""
		remove a product from cart
		"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		"""
		Iterate over the items in the cart and get the products from the databse
		"""
		product_ids = self.cart.keys()
		#get the product object
		products = Product.objects.filter(id__in = product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item ['total_price'] = item['price'] * item['quantity']
			yield item 

	def __len__(self):
		"""
		count all items in the cart
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		# remove cart from session
		del self.session['cart']
		self.session.modified = True