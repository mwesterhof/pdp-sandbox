from wagtail.core.models import Page
from wagtailtrans.models import TranslatablePage


class HomePage(TranslatablePage, Page):
    pass
