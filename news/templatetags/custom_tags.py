from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag
def make_posttype_url(post_type):
    return 'article' if post_type == 'AR' else 'news'


@register.simple_tag
def make_triple_dot(next_page, total):
    return '...' if total - next_page > 1 else ''


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()