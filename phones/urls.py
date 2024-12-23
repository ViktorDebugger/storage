from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', PhonesHome.as_view(), name='home'),
    path('add_phone/', AddPhone.as_view(), name='add_phone'),
    path('add_brand/', AddBrand.as_view(), name='add_brand'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('phone/<slug:phone_slug>/', ShowPhone.as_view(), name='phone'),
    path('brand/<slug:brand_slug>/', PhoneBrand.as_view(), name='brand'),
    path('orders', OrdersView.as_view(), name='orders'),
    path('selling', SellingView.as_view(), name='selling'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)