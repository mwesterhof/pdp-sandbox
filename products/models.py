from django.db import models
from wagtailtrans.models import TranslatablePage
from wagtail_app_pages.models import AppPageMixin


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductPage(AppPageMixin, TranslatablePage, models.Model):
    url_config = 'products.urls'
