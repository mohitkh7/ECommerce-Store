from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.bag_detail, name='bag-detail'),
	url(r'^add-to-bag/(?P<product_id>\d+)/$', views.add_to_bag, name='add-to-bag'),
	url(r'^remove-from-bag/(?P<product_id>\d+)/$', views.remove_from_bag, name='remove-from-bag'),

]