from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

SIZE_CHOICES = (
	("S","S"),
	("M","M"),
	("L","L"),
	("XL","XL"),
	("XXL","XXL"),
)

# Create your models here.
class Size(models.Model):
	short_name = models.CharField(max_length=5)
	long_name = models.CharField(max_length=30)
	length = models.IntegerField()

	def __str__(self):
		return self.short_name

class Color(models.Model):
	name = models.CharField(max_length=20)
	hex_code = models.CharField(max_length=7)

	def __str__(self):
		return "%s (%s)"%(self.name,self.hex_code)

class Category(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	slug = models.SlugField()

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.title

	#Overriding save method for slug field
	def save(self, *args, **kwargs):
		if not self.pk:
			# Newly created object, so set slug
			self.slug = slugify(self.title)
		
		super(Category, self).save(*args, **kwargs)

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	size = models.ManyToManyField(Size)
	color = models.ManyToManyField(Color) 

	image = models.ImageField()

	price = models.IntegerField()
	quantity = models.IntegerField()
	
	views = models.IntegerField(default = 0)
	updated_on = models.DateTimeField(auto_now_add = True)
	updated_by  = models.CharField(max_length=100) #User

	slug = models.SlugField(default="mohit")
	
	def __str__(self):
		return self.name

	#Overriding save method for slug field
	def save(self, *args, **kwargs):
		if not self.pk:
			# Newly created object, so set slug
			self.slug = slugify(self.name)
		
		super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('product',kwargs={'slug':self.slug,})

class ContactUs(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=300)
	message = models.TextField()
	received_on = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = "Contact Us"
	def __str__(self):
		return self.subject

class Offer(models.Model):
	pass

class Customer(models.Model):
	pass

class Wishlist(models.Model):
	pass

class Basket(models.Model):
	pass

class Order(models.Model):
	pass

class Review(models.Model):
	pass
