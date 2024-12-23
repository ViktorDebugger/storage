from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.utils.timezone import now

from .utils import *
from .models import *
from .forms import *

class PhonesHome(DataMixin, ListView):
    model = Phone
    template_name = 'phones/index.html'
    context_object_name = 'phones'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items())) 
    
    def get_queryset(self):
        return Phone.objects.all()
    
class AddPhone(DataMixin, CreateView):
    form_class = PhoneForm
    template_name = 'phones/addphone.html'
    success_url = reverse_lazy('home')
    raise_exception = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавлення телефону")
        return dict(list(context.items()) + list(c_def.items()))
    
class AddBrand(DataMixin, CreateView):
    form_class = BrandForm
    template_name = 'phones/addbrand.html'
    success_url = reverse_lazy('home')
    raise_exception = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавлення бренду")
        return dict(list(context.items()) + list(c_def.items()))
    
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')

class ShowPhone(DataMixin, DetailView):
    model = Phone
    template_name = 'phones/phone.html'
    slug_url_kwarg = 'phone_slug'
    context_object_name = 'phone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        c_def = self.get_user_context(title=context['phone'])
        if self.request.user.is_authenticated:
            context['form_title'] = "Зробити замовлення"
        else:
            context['form_title'] = "Замовлення (тільки для зареєстрованих користувачів)"
        return dict(list(context.items()) + list(c_def.items()))

    def post(self, request, *args, **kwargs):
        phone = self.get_object()
        form = OrderForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            order = Order(
                phone_id=phone,
                order_type="Закупівля для складу" if request.user.is_authenticated else "Закупівля для замовника",
                order_datetime=now(),
                quantity=quantity,
                total_price=phone.price * quantity
            )
            order.save()

            if request.user.is_authenticated:
                phone.quantity += quantity
            else:
                phone.quantity -= quantity

            phone.save()
            return redirect('home')

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    
class PhoneBrand(DataMixin, ListView):
    model = Phone
    template_name = 'phones/index.html'
    context_object_name = 'phones'
    allow_empty = False

    def get_queryset(self):
        return Phone.objects.filter(brand__slug=self.kwargs['brand_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Бренд - ' + str(context['phones'][0].brand),
                                      brand_selected=context['phones'][0].brand_id)
        return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'phones/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'phones/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class OrdersView(DataMixin, ListView):
    model = Order
    template_name = 'phones/orders.html'
    context_object_name = 'orders'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_type'] = 'Закупівля'

        c_def = self.get_user_context(title='Закупівля')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Order.objects.filter(order_type="Закупівля для складу")
    
class SellingView(DataMixin, ListView):
    model = Order
    template_name = 'phones/orders.html'
    context_object_name = 'orders'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_type'] = 'Продаж'
        c_def = self.get_user_context(title='Продаж')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Order.objects.filter(order_type="Закупівля для замовника")
