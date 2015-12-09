from django import template

from cms.templatetags.cms_tags import Placeholder
from laterpay import ItemDefinition

register = template.Library()


class PaidContentPlaceholder(Placeholder):

    name = 'lp_placeholder'

    def render_tag(self, context, name, extra_bits, nodelist=None):

        content = super(PaidContentPlaceholder, self).render_tag(context, name, extra_bits, nodelist)
        if not content:
            return content
        # TODO: how to determine whther the user has access to the content or not???
        request = context['request']
        page = request.current_page
        lp_client = request.laterpay
        item_def = ItemDefinition("{0}-{1}".format(page.id, name), "EUR99", "DE19", request.build_absolute_uri(), "Example Article 1000")
        url = lp_client.get_add_url(item_def)
        return '''<a href="#" data-laterpay="{0}" class="paylater">Use now pay later for 0,99 EUR</a>'''.format(url)

register.tag(PaidContentPlaceholder)
