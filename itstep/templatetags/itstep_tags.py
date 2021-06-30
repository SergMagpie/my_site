from django import template
from django.db.models import Count
from itstep.models import *

register = template.Library()


# @register.simple_tag(name='getcats')
# def get_categories():
#     return Category.objects.all()


@register.inclusion_tag('itstep/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.annotate(Count('exercises'))
    else:
        cats = Category.objects.annotate(Count('exercises')).order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}
