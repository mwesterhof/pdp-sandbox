from django.template import Library

from ..models import Category


register = Library()


@register.inclusion_tag(
    'products/templatetags/categories.html', takes_context=True)
def render_categories(context):
    page = context['self']
    context['categories'] = Category.objects.for_page(page)
    return context
