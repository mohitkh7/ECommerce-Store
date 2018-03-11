from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$',views.order_create,name='order-create'),
	# url(r'^detail/$',views.order_detail,name='order-detail'),
	url(r'^details/(?P<slug>[\w\-]+)/$',views.OrderDetail.as_view(),name='order-detail'),
	url(r'^track/$',views.order_track,name="order-track"),
]