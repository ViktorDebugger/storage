from django.db import models
from django.urls import reverse

class Phone(models.Model):
    OPERATING_SYSTEM_CHOICES = [
        ('Android', 'Android'),
        ('IOS', 'IOS'),
    ]    
    name = models.CharField(max_length=200, verbose_name="Назва телефону")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField(verbose_name="Ціна")
    quantity = models.IntegerField(default=0, verbose_name="Кількість на складі")
    screen_diagonal = models.FloatField(verbose_name="Діагональ екрана")
    battery_capacity = models.IntegerField(verbose_name="Ємність батареї")
    processor_cores = models.IntegerField(verbose_name="Кількість ядер процесора")
    operating_system = models.CharField(
        max_length=10, choices=OPERATING_SYSTEM_CHOICES, blank=True, verbose_name="Операційна система"
    )
    ram = models.IntegerField(verbose_name="Оперативна пам'ять (RAM)")
    rom = models.IntegerField(verbose_name="Вбудована пам'ять (ROM)")
    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, blank=True, verbose_name="Бренд", related_name="phones"
    )

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефони"
        
    def get_absolute_url(self):
        return reverse('phone', kwargs={'phone_slug': self.slug})    
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва бренду")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_slug': self.slug})


class Order(models.Model):
    OrderType = models.TextChoices("Закупівля для замовника", "Закупівля для складу")
    order_type = models.CharField(
        max_length=30, choices=OrderType, blank=True, verbose_name="Тип замовлення"
    )
    phone_id = models.ForeignKey(
        'Phone', on_delete=models.CASCADE, null=True, verbose_name="Телефон"
    )
    order_datetime = models.DateTimeField(verbose_name="Дата та час замовлення")
    quantity = models.IntegerField(verbose_name="Кількість")
    total_price = models.FloatField(verbose_name="Загальна ціна")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
