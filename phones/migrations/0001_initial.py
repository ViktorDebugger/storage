# Generated by Django 5.1 on 2024-12-19 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва бренду')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва телефону')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('quantity', models.IntegerField(default=0, verbose_name='Кількість на складі')),
                ('screen_diagonal', models.FloatField(verbose_name='Діагональ екрана')),
                ('battery_capacity', models.IntegerField(verbose_name='Ємність батареї')),
                ('processor_cores', models.IntegerField(verbose_name='Кількість ядер процесора')),
                ('operating_system', models.CharField(blank=True, choices=[('IOS', 'Ios')], max_length=10, verbose_name='Операційна система')),
                ('ram', models.IntegerField(verbose_name="Оперативна пам'ять (RAM)")),
                ('rom', models.IntegerField(verbose_name="Вбудована пам'ять (ROM)")),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='phones.brand', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефони',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(blank=True, choices=[('Закупівля', 'Закупівля'), ('для', 'Для'), ('складу', 'Складу')], max_length=30, verbose_name='Тип замовлення')),
                ('order_datetime', models.DateTimeField(verbose_name='Дата та час замовлення')),
                ('quantity', models.IntegerField(verbose_name='Кількість')),
                ('total_price', models.FloatField(verbose_name='Загальна ціна')),
                ('phone_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phones.phone', verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
    ]
