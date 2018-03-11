from .models import Category
from bag.views import count_net_item_in_bag
def navbar(request):
    ctx = {
        "all_categories": Category.objects.all(),
        "net_item_in_bag": count_net_item_in_bag(request),
    }
    return ctx