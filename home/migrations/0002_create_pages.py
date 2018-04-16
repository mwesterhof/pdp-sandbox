# -*- coding: utf-8 -*-
from django.db import migrations


class Migration(migrations.Migration):
    def create_pages(apps, schema_editor):
        ContentType = apps.get_model('contenttypes.ContentType')
        Page = apps.get_model('wagtailcore', 'Page')
        Site = apps.get_model('wagtailcore', 'Site')
        Language = apps.get_model('wagtailtrans', 'Language')
        TranslatableSiteRootPage = apps.get_model('wagtailtrans', 'TranslatableSiteRootPage')

        Page.objects.filter(depth__gt=1).delete()

        root = Page.objects.first()

        english, _ = Language.objects.get_or_create(
            code='en', defaults={'is_default': True, 'position': 0, 'live': True})

        trans_root_page = TranslatableSiteRootPage.objects.create(
            title="pdp test",
            slug="pdp-test",
            content_type=ContentType.objects.get_for_model(TranslatableSiteRootPage),
            path='{}0001'.format(root.path),
            depth=root.depth+1,
            numchild=0,
            url_path='/',
        )
        root.numchild = 1
        root.save()

        site = Site.objects.first()
        if not site:
            site = Site.objects.create(
                hostname='localhost:8000',
                port=80,
                site_name='pdp test',
                root_page=trans_root_page,
                is_default_site=True
            )
        else:
            site.root_page = trans_root_page
            site.save()

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailtrans', '0006_auto_20161212_2020'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pages, migrations.RunPython.noop)
    ]
