__author__ = 'destroyers34'
from django import template
register = template.Library()


@register.filter(name='prod_pourcent')
def prod_pourcent(obj, arg):
    return obj.pourcent_tache(arg)