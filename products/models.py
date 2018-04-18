from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, ObjectList, StreamFieldPanel, TabbedInterface)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail_app_pages.models import AppPageMixin
from wagtailtrans.models import TranslatablePage

from .blocks import OrderProductCTABlock, ParagraphBlock
from .managers import CategoryManager


class Category(models.Model):
    name = models.CharField(max_length=200)

    objects = CategoryManager()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductPage(AppPageMixin, TranslatablePage, Page):
    url_config = 'products.urls'

    pop_content = StreamField([
        ('paragraph', ParagraphBlock()),
    ], blank=True, null=True)

    pdp_content = StreamField([
        ('paragraph', ParagraphBlock()),
        ('order_product_cta', OrderProductCTABlock()),
    ], blank=True, null=True)

    edit_handler = TabbedInterface([
        ObjectList([
            FieldPanel('title'),
            StreamFieldPanel('pop_content')
        ], heading="POP"),
        ObjectList([
            StreamFieldPanel('pdp_content')
        ], heading="PDP"),
        ObjectList(TranslatablePage.promote_panels, heading="Promote"),
        ObjectList(
            TranslatablePage.settings_panels + [
                InlinePanel('categories', label="Categories"),
            ],
            heading="Settings"),
    ])


class PageCategory(models.Model):
    category = models.ForeignKey(
        Category, related_name='pages', on_delete=models.CASCADE)

    product_page = ParentalKey(
        ProductPage, related_name='categories', on_delete=models.CASCADE)
