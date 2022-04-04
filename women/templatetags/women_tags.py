from django import template
from women.models import *
from django .db.models import Count

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    #cats = Category.objects.all()
    cats=Category.objects.annotate(cnt=Count('women')).filter(cnt__gt=0)
    return {"cats": cats}