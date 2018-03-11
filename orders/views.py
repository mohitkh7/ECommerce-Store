from django.shortcuts import render, reverse, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from bag.views import get_bag
from django.http import HttpResponse
from django.views import generic
# Create your views here.
def order_create(request):
	bag,bag_properties = get_bag(request)
	print("inside order_create")
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			print("inside valid form")
			order = form.save()
			for item in bag:
				OrderItem.objects.create(order=order,product=item.product,price=item.price,quantity=item.quantity)
				item.is_ordered = True
				item.save()
			return render(request,'order_complete.html')
	else:
		form = OrderCreateForm()
	return render(request,'order_create.html',{'form':form,'bag':bag,'bag_properties':bag_properties})

class OrderDetail(generic.DetailView):
	model = Order
	slug_field = 'token'
	template_name = 'order_detail.html'
	context_object_name = 'order'

def order_detail(request):
	return render(request,"order_complete.html")

def order_track(request):
	if request.method == "POST":
		token = request.POST.get('token')
		email = request.POST.get('email')
		try:
			order = Order.objects.get(token=token,email=email)
		except:
			is_error = True 
			return render(request,'order_track.html',{'is_error':is_error})
		return redirect(reverse('orders:order-detail',kwargs={'slug':order.token,}))
	return render(request,'order_track.html')
