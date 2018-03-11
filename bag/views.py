from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Sum

from web.models import Product
from .models import Bag

import random

# Create your views here.
def get_bag_properties(bag):

	bag_properties = {'net_price':0,'net_item':0,'net_quantity':0}
	for item in bag:
		bag_properties['net_item'] += 1
		bag_properties['net_quantity'] += item.quantity
		bag_properties['net_price'] += item.price * item.quantity
	return bag_properties

def bag_detail(request):
	bag = Bag.objects.filter(customer_id=get_customer_id(request),is_removed=False,is_ordered = False)
	bag_properties = get_bag_properties(bag)

	return render(request,"bag.html",{'bag':bag,'bag_properties':bag_properties})

def add_to_bag(request,product_id):
	customer_id = get_customer_id(request)
	product = Product.objects.get(id=product_id)
	bag,created =  Bag.objects.get_or_create(customer_id=customer_id,product=product,is_ordered=False)
	#A new bag is created
	if created:
		bag.price = product.price

	#bag already exist
	else:
		if bag.is_removed == True:
			bag.price = product.price
			bag.quantity = 1
			bag.is_removed = False
		elif bag.is_ordered == True:
			bag.price = product.price
			bag.quantity = 1
			bag.is_ordered = False
		else:
			bag.quantity += 1
	bag.save()
	return redirect("bag:bag-detail")

def remove_from_bag(request,product_id):
	customer_id = get_customer_id(request)
	product = Product.objects.get(id=product_id)
	try:
		bag = Bag.objects.get(customer_id=customer_id,product=product,is_ordered=False)
	except:
		return redirect("home")
	bag.is_removed = True
	bag.save()
	return redirect("bag:bag-detail")
	

def get_customer_id(request):
	#User is logged in
	if request.user.is_authenticated():
		return request.user.id

	#Session is already set
	if request.session.get('unique_session_id'):
		return request.session.get('unique_session_id')

	#Set Session
	else:
		request.session['unique_session_id'] = unique_number_generator()
		return request.session.get('unique_session_id')

def unique_number_generator():
	number = ''
	characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	number_length = 50
	for y in range(number_length):
		number += characters[random.randint(0, len(characters)-1)]
	return number

def count_net_item_in_bag(request):
	bag = Bag.objects.filter(customer_id=get_customer_id(request),is_removed=False,is_ordered = False)
	return bag.count()

def get_bag(request):
	bag = Bag.objects.filter(customer_id=get_customer_id(request),is_removed=False,is_ordered = False)
	bag_properties = get_bag_properties(bag)
	return bag, bag_properties