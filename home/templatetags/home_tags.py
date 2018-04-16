from collections import namedtuple
from django.template import Library
from wagtailtrans.models import get_user_language

from ..models import HomePage


register = Library()


PageNode = namedtuple('PageNode', ['page', 'is_active'])
TranslationNode = namedtuple('TranslationNode', ['language', 'url'])


@register.inclusion_tag('home/templatetags/menu.html', takes_context=True)
def render_menu(context):
    language = get_user_language(context['request'])
    home = HomePage.objects.get(language=language)
    current_page = context.get('page', home)
    child_pages = home.get_children().specific()

    if home.live:
        child_pages = child_pages.live()

    nodes = [
        PageNode(page, page == current_page)
        for page in [home] + list(child_pages)
    ]

    return {
        'nodes': nodes
    }


@register.inclusion_tag(
    'home/templatetags/language_selector.html', takes_context=True)
def render_language_selector(context):
    current = context['page'].specific
    translations = current.get_translations()
    context['translations'] = [
        TranslationNode(page.language, page.url)
        for page in translations
    ]

    return context
