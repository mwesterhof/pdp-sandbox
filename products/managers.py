from django.db import models


class CategoryManager(models.Manager):
    def for_page(self, page):
        return super().get_queryset().filter(pages__product_page=page)
