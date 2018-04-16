from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import Category, Product


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_icon = 'folder'
    menu_label = 'Categories'


class ProductAdmin(ModelAdmin):
    model = Product
    menu_icon = 'pick'
    menu_label = 'Products'
    list_display = ('__str__', 'category')
    list_filter = ('category',)


class ProductsGroup(ModelAdminGroup):
    items = [CategoryAdmin, ProductAdmin]
    menu_icon = 'cog'
    menu_label = 'Products'


modeladmin_register(ProductsGroup)
