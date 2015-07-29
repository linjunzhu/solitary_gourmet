# -*- encoding=utf-8 -*-
from django import template
import pdb
register = template.Library()

@register.filter(name='show')
def show(value):
    if value:
        return value
    else:
        return ""

@register.filter(name='show_url')
def show_url(value):
    if value:
        return value.url
    else:
        return ""