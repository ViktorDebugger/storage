from django.db.models import Count
from .models import *

menu = [{'title': "Головна сторінка", 'url_name': 'home'},
        {'title': "Добавити телефон", 'url_name': 'add_phone'},
        {'title': "Добавити бренд", 'url_name': 'add_brand'},
        {'title': "Закупівля", 'url_name': 'orders'},
        {'title': "Продаж", 'url_name': 'selling'},
]

class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        brands = Brand.objects.annotate(phone_count=Count('phones'))
        context['brands'] = brands

        user_menu = menu.copy()
        
        context['menu'] = user_menu
        
        if 'brand_selected' not in context:
            context['brand_selected'] = 0
        return context