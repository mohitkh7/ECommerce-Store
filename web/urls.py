from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.Home.as_view(),name="home"),
	url(r'product/(?P<slug>[\w\-]+)/$',views.ProductDetail.as_view(),name="product"),

	url(r'all-products/$',views.ProductList.as_view(),name="all-products"),
	url(r'category/(?P<slug>[\w\-]+)/$',views.CategoryDetail.as_view(),name="category-detail"),
	# url(r'add-to-cart/$',views.AddToCart.as_view(),name="add-to-cart"),
	url(r'add-to-cart/$',views.add_to_cart,name="add-to-cart"),

	url(r'^about-us/$',views.AboutUs.as_view(),name="about-us"),
	url(r'^contact-us/$',views.ContactUs.as_view(),name="contact-us"),
]