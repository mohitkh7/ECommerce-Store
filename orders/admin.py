from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
	model = OrderItem

class OrderAdmin(admin.ModelAdmin):
	inlines = [OrderItemInline,]
	list_display = ['token','name','email','created','total_price','paid',]
	search_fields = ('token',)


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('product','quantity','get_token')

	def get_token(self,obj):
		return obj.order.token
	get_token.admin_order_field = "order"
	get_token.short_description = "Order"


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)