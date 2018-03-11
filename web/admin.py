from django.contrib import admin
from .models import Product,Category,Size,Color,ContactUs
from django.contrib.sessions.models import Session

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','quantity','price','views',]
	list_filter = ('category',)
	search_fields = ('name',)
	ordering = ('price','views',)
	date_hierarchy = 'updated_on'
	# prepopulated_fields = {'slug':('name',)}

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ContactUs)
admin.site.register(Session,SessionAdmin)