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
        request = context['request']

        # for now show the content to the logged in user
        # TODO: check with django-cms permissions
        if request.user.is_authenticated():
            return content
        page = request.current_page
        lp_client = request.laterpay

        article_id = "{0}-{1}".format(page.id, name)

        data = lp_client.get_access(article_id)
        article_acces = data.get('articles', {}).get(article_id, {}).get('access', False)

        if article_acces is True:
            return content

        item_def = ItemDefinition(item_id=article_id,
                                  pricing="EUR99",
                                  url=request.build_absolute_uri(),
                                  title="Example Article 1000",
                                  cp=lp_client.cp_key
                                  )

        url = lp_client.get_add_url(item_def)
        return '''<a href="#" data-laterpay="{0}" class="paylater">Use now pay later for 0,99 EUR</a>'''.format(url)

register.tag(PaidContentPlaceholder)
