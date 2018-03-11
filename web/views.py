from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views import View, generic
from django.views.generic.edit import CreateView

from .models import Product, Category

from .forms import ContactUsForm
from cart.forms import CartAddProductForm
# Create your views here.

class Home(View):
	template_name = "index.html"

	def get(self,request):
		# print("\n\n\nsession =>",request.session['cart'])
		products = Product.objects.all()
		return render(request,self.template_name,{'products':products,})

class ProductDetail(generic.DetailView):
	model = Product
	template_name = "product_detail.html"
	cart_product_form = CartAddProductForm()

	def get_context_data(self, **kwargs):
		context = super(ProductDetail, self).get_context_data(**kwargs)
		context['similar_products'] = Product.objects.all()
		context['cart_product_form'] = self.cart_product_form
		return context

	def get_object(self):
		# Call the superclass
		object = super(ProductDetail, self).get_object()
		# Update the views everytime this product is viewed
		object.views = object.views + 1
		object.save()
		# Return the object
		return object

class ProductList(generic.ListView):
	model = Product
	template_name = "all_products.html"
	context_object_name = "all_products"

class CategoryDetail(generic.DetailView):
	model = Category
	template_name = "category_detail.html"

def add_to_cart(request):
	print("inside")
	request.session['dash'] = "mohit"
	return HttpResponse("Mohit")

class AboutUs(View):
	template_name = "aboutus.html"
	def get(self,request):
		return render(request,self.template_name)

class ContactUs(CreateView):
	template_name = "contactus.html"
	form_class = ContactUsForm
	success_url = reverse_lazy("home")