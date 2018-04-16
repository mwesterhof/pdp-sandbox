from django.views.generic import DetailView, ListView

from .models import Product


class ProductViewMixin:
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['page'] = ctx['self'] = self.parent_page
        return ctx


class ProductList(ProductViewMixin, ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        category = self.request.GET.get('category')
        if category:
            return qs.filter(category=category[0])
        return qs


class ProductDetail(ProductViewMixin, DetailView):
    model = Product
