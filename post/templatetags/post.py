from django import template
register = template.Library()

"""
{% ํ๊ทธ ''%}
{{value|ํํฐ}}
"""

from post.models import *
@register.simple_tag
def print_post_list():
    return Post.objects.all()