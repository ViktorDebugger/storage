from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

from django import forms
from .models import Phone, Brand, Order

class PhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].empty_label = "Не вибрано"
        
    operating_system = forms.ChoiceField(
        choices=[('', 'Не вибрано')] + Phone.OPERATING_SYSTEM_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Операційна система'
    )
    
    class Meta:
        model = Phone
        fields = [
            'name', 'photo', 'slug', 'price', 'quantity', 'screen_diagonal', 
            'battery_capacity', 'processor_cores', 'operating_system', 
            'ram', 'rom', 'brand'
        ]
        labels = {
            'name': "Назва телефону",
            'photo': "Фото",
            'slug': "URL",
            'price': "Ціна",
            'quantity': "Кількість на складі",
            'screen_diagonal': "Діагональ екрана",
            'battery_capacity': "Ємність батареї",
            'processor_cores': "Кількість ядер процесора",
            'ram': "Оперативна пам'ять (RAM)",
            'rom': "Вбудована пам'ять (ROM)",
            'brand': "Бренд",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'form-control'}),
            'battery_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'processor_cores': forms.NumberInput(attrs={'class': 'form-control'}),
            'operating_system': forms.Select(attrs={'class': 'form-control'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control'}),
            'rom': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'slug']
        labels = {
            'name': "Назва бренду",
            'slug': "URL",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        label='Кількість'
    )
    
class RegisterUserForm(UserCreationForm):
    usable_password = None
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
