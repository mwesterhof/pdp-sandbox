from django.template import Library

from ..models import Category


register = Library()


@register.inclusion_tag(
    'products/templatetags/categories.html', takes_context=True)
def render_categories(context):
    context['categories'] = Category.objects.all()
    return context
