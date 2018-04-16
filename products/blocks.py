from string import Template

from wagtail.core import blocks


class OrderProductCTABlock(blocks.StructBlock):
    PLACEHOLDER_HELP = "Use $product to refer to the product name"

    title = blocks.CharBlock(help_text=PLACEHOLDER_HELP)
    body = blocks.TextBlock(help_text=PLACEHOLDER_HELP)
    cta_text = blocks.CharBlock(help_text=PLACEHOLDER_HELP)

    class Meta:
        template = 'products/blocks/order_product_cta.html'

    def _substitute(self, value, product):
        return {
            k: Template(v).substitute(product=product)
            for k, v in value.items()
        }

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)

        value = ctx['value']
        product = ctx['product']
        ctx.update({
            'substituted': self._substitute(value, product)
        })

        return ctx


class ParagraphBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock()

    class Meta:
        template = 'products/blocks/paragraph.html'
