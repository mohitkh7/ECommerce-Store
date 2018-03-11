from django.contrib import admin

from .models import Bag #importing models

# Register your models here.
# admin.site.register(Bag)

@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
	list_display = ('product','customer_id','quantity','price','is_removed','is_ordered','added_on','modified_on')
